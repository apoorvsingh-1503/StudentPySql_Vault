# Student Grade Management System

A console-based **Student Grade Management System** built with **Python and SQLite**. The system provides separate Admin and Student interfaces for managing student information, subjects, marks, attendance, and communication.

## Features

### Admin

* Create and log in as an Admin
* Create student accounts
* Delete students
* Add student subjects
* Add student marks
* Update student attendance
* View messages sent by students
* Add another Admin
* Change Admin password

### Student

* Student login
* View marks
* View attendance
* View personal details
* View subject details
* Send messages to Admin
* Change password

## Project Structure

```text
StudentGrade/
│
├── main.py              # Program entry point
├── Admin.py             # Admin operations
├── Student.py           # Student operations
├── utils.py             # SQLite database functions
├── requirements.txt     # Project dependencies
├── .gitignore           # Git ignored files
└── student.sqlite3      # Local SQLite database
```

## Technologies Used

* **Python 3**
* **SQLite3**
* **Object-Oriented Programming**
* **SQL**
* **Modular Programming**

## Requirements

* Python 3.x
* SQLite3

SQLite3 is included with Python, so no external packages are required.

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd StudentGrade
```

### 3. Run the application

```bash
python main.py
```

## Main Menu

```text
=== WELCOME TO APOORV STUDENT SYSTEM ===

1. ADMIN LOGIN
2. STUDENT LOGIN
q. QUIT
```

### Admin Dashboard

The Admin can:

```text
1. ADD STUDENT
2. ADD STUDENT ATTENDANCE
3. ADD STUDENT'S SUBJECTS
4. ADD STUDENT'S MARKS
5. DELETE STUDENT
6. SEE STUDENT MESSAGE
7. ADD ADMIN
8. CHANGE PASSWORD
9. LOGOUT
```

### Student Dashboard

The Student can:

```text
1. SEE MARKS
2. SEE ATTENDANCE
3. SEE YOUR FULL DETAIL
4. MESSAGE ADMIN
5. PASSWORD CHANGE
6. LOGOUT
```

## Database

The application uses an SQLite database named:

```text
student.sqlite3
```

The database stores information related to:

* Admins
* Students
* Subjects
* Marks
* Attendance
* Messages

The database file is excluded from Git using `.gitignore` so local database records are not accidentally uploaded to GitHub.

## Module Description

### `main.py`

Handles the main application menu and directs the user to either Admin or Student login.

### `Admin.py`

Contains all Admin-related functionality, including student creation, marks, subjects, attendance, messages, and account management.

### `Student.py`

Contains all Student-related functionality, including login, viewing marks and attendance, viewing details, messaging Admin, and password changes.

### `utils.py`

Contains the SQLite database connection and reusable database query function.

## Security Note

This project is designed as a **learning/academic project**. Authentication currently uses simple credentials and is not intended for production use.

For a production system, passwords should be securely hashed and sensitive information should not be displayed or stored as plain text.

## Future Improvements

* Password hashing
* Input validation
* Automatic grade calculation
* Percentage calculation
* Student search
* Admin/student profile management
* Better error handling
* GUI or web interface
* Database initialization script
* Improved database relationships

## Author

**Apoorv Singh**

GitHub: `https://github.com/apoorvsingh-1503`

---

⭐ If you find this project useful, consider giving the repository a star!
