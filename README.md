# ☁️ Data Redundancy Removal System

A cloud-oriented data management application developed as part of the **CodeAlpha Cloud Computing Internship**.

The system detects duplicate user records before storing them and allows only verified unique data to be added to the database.

## 🎯 Project Objective

The main objective is to maintain accurate and efficient cloud data by:

* Detecting duplicate records
* Validating incoming data against existing records
* Preventing duplicate data from being stored
* Storing only unique and verified records
* Tracking duplicate attempts

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **SQLite**
* **HTML5**
* **CSS3**
* **Jinja2**
* **Git & GitHub**

## ⚙️ How It Works

```text
User enters data
       ↓
System validates the data
       ↓
Check existing database records
       ↓
   ┌───────────────┐
   │ Duplicate?    │
   └───────┬───────┘
           │
      ┌────┴────┐
      │         │
     YES        NO
      │         │
      ↓         ↓
Reject data   Store data
      │         │
      ↓         ↓
Log duplicate  Verified
attempt        unique record
```

## 🔍 Key Features

### 1. Duplicate Detection

The system checks whether the submitted email or phone number already exists.

### 2. Duplicate Prevention

Duplicate records are rejected before insertion into the database.

### 3. Unique Data Storage

Only verified unique records are stored in the `users` table.

### 4. Duplicate Attempt Tracking

Rejected duplicate submissions are recorded in the `duplicate_attempts` table.

### 5. Dashboard

The application displays:

* Total Verified Records
* Unique Records
* Duplicates Prevented

### 6. Responsive Interface

The web interface is designed to work on desktop and smaller screens.

## 📂 Project Structure

```text
CodeAlpha_DataRedundancyRemoval/
│
├── app.py
├── database.db
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── .venv/
```

## 🚀 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/CodeAlpha_DataRedundancyRemoval.git
```

### Step 2: Open the project

```bash
cd CodeAlpha_DataRedundancyRemoval
```

### Step 3: Create a virtual environment

```bash
python -m venv .venv
```

### Step 4: Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## 🧪 Testing

The application was tested using:

### Unique Record

A new user with a unique email and phone number is successfully stored.

### Duplicate Record

Submitting an existing email or phone number is rejected.

The dashboard updates the **Duplicates Prevented** count after a duplicate attempt.

## 📌 Internship Task

**CodeAlpha Cloud Computing Internship**

**Task:** Data Redundancy Removal System

The project demonstrates data validation, duplicate detection, database management, and a web-based cloud-oriented application workflow.

## 👩‍💻 Developer

**Niharika Chandana**

Developed as part of the CodeAlpha Cloud Computing Internship.
