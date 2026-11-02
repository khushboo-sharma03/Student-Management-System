STUDENT MANAGEMENT SYSTEM
Python Mini Project | Tkinter + SQLite

1. PROJECT OVERVIEW
This desktop application helps manage student information. It provides a simple
interface to add, view, search, update and delete student records.

2. TECHNOLOGIES
- Python 3
- Tkinter (GUI)
- SQLite3 (database; included with standard Python)

3. REQUIREMENTS
- Python 3 installed
- VS Code or Python IDLE (optional)
No third-party Python packages are required.

4. HOW TO RUN ON WINDOWS
1. Extract Student_Management_System.zip.
2. Open the extracted folder in VS Code.
3. Open Terminal > New Terminal.
4. Run: py main.py
   You can also try: python main.py
5. The application window will open. The database file students.db is
   automatically created in the same folder when the program starts.

5. FEATURES
- Add student details
- View all student records
- Update an existing record (select a row first)
- Delete a record (select a row first and confirm)
- Search by roll number, name, email, phone, course or semester
- Input validation for required fields, email and phone
- Prevent duplicate roll numbers
- Store records permanently in SQLite database

6. HOW TO USE
ADD: Fill the form and click Add Student.
UPDATE: Click a student row in the table, edit the form, then click Update.
DELETE: Select a student row and click Delete.
SEARCH: Type in the search box or click Search.
SHOW ALL: Click Show All to display every saved record.
CLEAR: Click Clear to empty the form.

7. DATABASE TABLE
Table name: students
Fields:
- id: Integer primary key (auto generated)
- roll_no: Unique student roll number
- name: Student name
- email: Email address
- phone: Phone number
- course: Course name
- semester: Semester number

8. PYTHON CONCEPTS USED
- Functions and classes
- Tkinter widgets and event handling
- SQLite database operations
- SQL INSERT, SELECT, UPDATE and DELETE
- Conditional statements
- Exception handling
- Input validation and regular expressions

9. PROJECT STRUCTURE
Student_Management_System/
    main.py
    README.txt
    PROJECT_REPORT.md
    requirements.txt
    students.db (created automatically after first run)

10. NOTE
Use sample/student data for demonstration. Keep a backup of students.db if
you need to preserve your records.
