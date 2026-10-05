# ADT_AdvProg_Sep26_StaffDirectory

# Staff Directory — Flask App
A simple staff directory web app built with Flask, SQLite, and a RESTful API.

---
## Project Structure
```
staff_directory/
├── app.py                  # Flask app, database model, REST API
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── templates/
    └── index.html          # Front-end (HTML + vanilla JS)
```
The SQLite database file (`staff.db`) is created automatically when you first run the app.
---

## Quick Start

OPEN IN CODESPACES!!!!!

Ensure python extension is installed!

Then....
### 1. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

Then open your browser and go to: **http://127.0.0.1:5000**

The database is created automatically and loaded with 10 sample staff members on first run.
---

## REST API Reference

| Method | Endpoint            | Description          |
|--------|---------------------|----------------------|
| GET    | `/api/staff`        | Get all staff        |
| POST   | `/api/staff`        | Add a staff member   |
| PUT    | `/api/staff/<id>`   | Update a staff member|
| DELETE | `/api/staff/<id>`   | Delete a staff member|

### Example POST body (JSON)
```json
{
  "name": "Jane Smith",
  "role": "Business Analyst",
  "department": "Operations"
}
```

---

## Features

- List all staff in a clean table
- Add new staff using the form
- Edit any staff member (form pre-fills automatically)
- Delete staff with a confirmation prompt
- All changes saved instantly to SQLite via the REST API
- No external JS frameworks — just vanilla JavaScript
