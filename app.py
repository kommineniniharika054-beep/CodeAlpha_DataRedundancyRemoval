from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "codealpha-secret-key"


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE
        )
    """)

    # Duplicate attempts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS duplicate_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            phone TEXT
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Get verified users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    # Total verified records
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # Total duplicate attempts prevented
    cursor.execute("SELECT COUNT(*) FROM duplicate_attempts")
    duplicate_count = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        users=users,
        total_users=total_users,
        duplicate_count=duplicate_count
    )


@app.route("/add", methods=["POST"])
def add_user():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Check for existing email or phone
    cursor.execute(
        "SELECT * FROM users WHERE email = ? OR phone = ?",
        (email, phone)
    )

    existing_user = cursor.fetchone()

    if existing_user:

        # Record duplicate attempt
        cursor.execute(
            """
            INSERT INTO duplicate_attempts (email, phone)
            VALUES (?, ?)
            """,
            (email, phone)
        )

        conn.commit()
        conn.close()

        flash(
            "Duplicate data detected! Record was prevented from being added.",
            "error"
        )

        return redirect(url_for("home"))

    # Add only unique data
    cursor.execute(
        """
        INSERT INTO users (name, email, phone)
        VALUES (?, ?, ?)
        """,
        (name, email, phone)
    )

    conn.commit()
    conn.close()

    flash(
        "User verified successfully! Unique data added.",
        "success"
    )

    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)