# STUDENT MANAGEMENT SYSTEM
## Mini Project Report

**Subject:** Python Programming  
**Project Title:** Student Management System  
**Technology Used:** Python, Tkinter and SQLite

---

## 1. Introduction
The Student Management System is a desktop-based application developed in Python.
It is designed to store and manage student information in an organized way.
The application provides a graphical user interface so that users can perform
basic student-record operations without writing SQL commands.

## 2. Objectives
- To maintain student records digitally.
- To reduce manual record-keeping.
- To add, display, search, update and delete student details.
- To store information in a local database.
- To practice Python GUI and database connectivity.

## 3. Software and Hardware Requirements
**Software**
- Python 3
- Tkinter GUI library
- SQLite3 database
- Windows, Linux or macOS
- VS Code or Python IDLE

**Hardware**
- Computer or laptop
- Minimum 2 GB RAM recommended
- Basic disk space for Python and project files

## 4. Modules
1. **Add Student:** Saves a new student's roll number, name, email, phone,
   course and semester.
2. **View Students:** Displays saved student records in a table.
3. **Search Student:** Finds records using roll number, name, email, phone,
   course or semester.
4. **Update Student:** Updates the selected student's details.
5. **Delete Student:** Removes the selected record after confirmation.
6. **Clear Form:** Clears the input fields.

## 5. Database Design
The application uses an SQLite table named `students`.

| Field | Data type | Description |
|---|---|---|
| id | INTEGER | Primary key, auto increment |
| roll_no | TEXT | Unique roll number |
| name | TEXT | Student name |
| email | TEXT | Email address |
| phone | TEXT | Contact number |
| course | TEXT | Course name |
| semester | TEXT | Semester |

## 6. Working
When the application starts, it creates the database and students table if they
do not already exist. The user enters details in the form and chooses an action.
The application validates the input and executes the corresponding SQL query.
The table is refreshed to show the latest records.

## 7. Python Concepts Used
- Variables, functions and classes
- Tkinter labels, entries, buttons, frames and Treeview
- Event handling
- SQLite database connectivity
- SQL commands: INSERT, SELECT, UPDATE and DELETE
- Conditional statements and exception handling
- Regular expressions for input validation

## 8. Advantages
- Easy-to-use graphical interface
- Faster record searching
- Data is stored persistently
- Duplicate roll numbers are prevented
- No separate database server is required

## 9. Limitations
- The project is designed for local, single-computer use.
- It does not include login or role-based access.
- It does not provide cloud synchronization.

## 10. Future Scope
- Add user login and administrator roles.
- Add attendance and marks management.
- Export student records to CSV or PDF.
- Add a student photo and address field.
- Create a web-based version for multiple users.

## 11. Conclusion
The Student Management System demonstrates how Python GUI programming can be
combined with SQLite to build a useful record-management application. It
successfully performs the basic operations of adding, viewing, searching,
updating and deleting student records.

## 12. How to Execute
1. Install Python 3.
2. Extract the project ZIP.
3. Open the project folder in VS Code.
4. Run `py main.py` in the terminal.
5. The application window will open. The database is created automatically.
