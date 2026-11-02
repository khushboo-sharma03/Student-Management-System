import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import re

DB_NAME = "students.db"


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1050x650")
        self.root.minsize(900, 580)
        self.root.configure(bg="#f3f6fb")

        self.selected_student_id = None
        self.create_database()
        self.build_interface()
        self.load_students()

    def connect_db(self):
        return sqlite3.connect(DB_NAME)

    def create_database(self):
        with self.connect_db() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    roll_no TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    course TEXT NOT NULL,
                    semester TEXT NOT NULL
                )
            """)

    def build_interface(self):
        header = tk.Frame(self.root, bg="#243b6b", height=85)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="STUDENT MANAGEMENT SYSTEM",
            font=("Arial", 22, "bold"), bg="#243b6b", fg="white"
        ).pack(pady=(15, 2))
        tk.Label(
            header, text="Add  •  View  •  Update  •  Delete  •  Search Student Records",
            font=("Arial", 10), bg="#243b6b", fg="#dce6ff"
        ).pack()

        body = tk.Frame(self.root, bg="#f3f6fb")
        body.pack(fill="both", expand=True, padx=18, pady=16)

        form = tk.LabelFrame(
            body, text=" Student Details ", font=("Arial", 12, "bold"),
            bg="white", fg="#243b6b", padx=15, pady=12
        )
        form.pack(side="left", fill="y", padx=(0, 15))

        self.entries = {}
        fields = [
            ("Roll Number", "roll_no"),
            ("Student Name", "name"),
            ("Email Address", "email"),
            ("Phone Number", "phone"),
        ]

        for row, (label, key) in enumerate(fields):
            tk.Label(form, text=label, font=("Arial", 10, "bold"),
                     bg="white", fg="#333333").grid(
                row=row * 2, column=0, sticky="w", pady=(7, 3)
            )
            entry = tk.Entry(form, font=("Arial", 11), width=27,
                             relief="solid", bd=1)
            entry.grid(row=row * 2 + 1, column=0, ipady=6, sticky="ew")
            self.entries[key] = entry

        tk.Label(form, text="Course", font=("Arial", 10, "bold"),
                 bg="white", fg="#333333").grid(
            row=8, column=0, sticky="w", pady=(7, 3)
        )
        self.course_var = tk.StringVar()
        self.course_box = ttk.Combobox(
            form, textvariable=self.course_var, width=25,
            values=("BCA", "BBA", "B.Tech", "MCA", "MBA", "B.Sc", "Other"),
            state="readonly", font=("Arial", 10)
        )
        self.course_box.grid(row=9, column=0, sticky="ew", ipady=4)

        tk.Label(form, text="Semester", font=("Arial", 10, "bold"),
                 bg="white", fg="#333333").grid(
            row=10, column=0, sticky="w", pady=(7, 3)
        )
        self.semester_var = tk.StringVar()
        self.semester_box = ttk.Combobox(
            form, textvariable=self.semester_var, width=25,
            values=("1", "2", "3", "4", "5", "6", "7", "8"),
            state="readonly", font=("Arial", 10)
        )
        self.semester_box.grid(row=11, column=0, sticky="ew", ipady=4)

        button_frame = tk.Frame(form, bg="white")
        button_frame.grid(row=12, column=0, sticky="ew", pady=(18, 5))
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        self.make_button(button_frame, "Add Student", self.add_student,
                         "#198754").grid(row=0, column=0, sticky="ew", padx=3, pady=4)
        self.make_button(button_frame, "Update", self.update_student,
                         "#2864c7").grid(row=0, column=1, sticky="ew", padx=3, pady=4)
        self.make_button(button_frame, "Delete", self.delete_student,
                         "#c0392b").grid(row=1, column=0, sticky="ew", padx=3, pady=4)
        self.make_button(button_frame, "Clear", self.clear_form,
                         "#64748b").grid(row=1, column=1, sticky="ew", padx=3, pady=4)

        right = tk.Frame(body, bg="#f3f6fb")
        right.pack(side="right", fill="both", expand=True)

        top = tk.Frame(right, bg="#f3f6fb")
        top.pack(fill="x", pady=(0, 10))
        tk.Label(top, text="Student Records", font=("Arial", 15, "bold"),
                 bg="#f3f6fb", fg="#243b6b").pack(side="left")

        search_frame = tk.Frame(top, bg="#f3f6fb")
        search_frame.pack(side="right")
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var,
                                 font=("Arial", 10), width=22, relief="solid", bd=1)
        search_entry.pack(side="left", ipady=5, padx=(0, 5))
        search_entry.bind("<KeyRelease>", lambda event: self.search_students())
        self.make_button(search_frame, "Search", self.search_students,
                         "#2864c7").pack(side="left", padx=2)
        self.make_button(search_frame, "Show All", self.show_all_students,
                         "#64748b").pack(side="left", padx=2)

        table_frame = tk.Frame(right, bg="white", bd=1, relief="solid")
        table_frame.pack(fill="both", expand=True)

        columns = ("id", "roll_no", "name", "email", "phone", "course", "semester")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings",
                                 selectmode="browse")
        headings = {
            "id": "ID", "roll_no": "Roll No.", "name": "Student Name",
            "email": "Email", "phone": "Phone", "course": "Course",
            "semester": "Sem."
        }
        widths = {"id": 45, "roll_no": 85, "name": 135, "email": 160,
                  "phone": 105, "course": 85, "semester": 55}
        for col in columns:
            self.tree.heading(col, text=headings[col])
            self.tree.column(col, width=widths[col], anchor="center")

        y_scroll = ttk.Scrollbar(table_frame, orient="vertical",
                                 command=self.tree.yview)
        x_scroll = ttk.Scrollbar(table_frame, orient="horizontal",
                                 command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

        self.status_var = tk.StringVar(value="Ready")
        status = tk.Label(right, textvariable=self.status_var, anchor="w",
                          bg="#f3f6fb", fg="#555555", font=("Arial", 9))
        status.pack(fill="x", pady=(8, 0))

    @staticmethod
    def make_button(parent, text, command, color):
        return tk.Button(
            parent, text=text, command=command, bg=color, fg="white",
            activebackground=color, activeforeground="white",
            font=("Arial", 9, "bold"), relief="flat", padx=9, pady=7,
            cursor="hand2"
        )

    def get_form_data(self):
        data = {key: widget.get().strip() for key, widget in self.entries.items()}
        data["course"] = self.course_var.get().strip()
        data["semester"] = self.semester_var.get().strip()

        if not data["roll_no"] or not data["name"] or not data["course"] or not data["semester"]:
            messagebox.showwarning(
                "Missing Information",
                "Please enter Roll Number, Student Name, Course and Semester."
            )
            return None

        if data["email"] and not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", data["email"]):
            messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
            return None

        if data["phone"] and not re.fullmatch(r"[0-9+\-\s()]{7,20}", data["phone"]):
            messagebox.showwarning("Invalid Phone", "Please enter a valid phone number.")
            return None

        return data

    def add_student(self):
        data = self.get_form_data()
        if not data:
            return
        try:
            with self.connect_db() as conn:
                conn.execute("""
                    INSERT INTO students (roll_no, name, email, phone, course, semester)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (data["roll_no"], data["name"], data["email"], data["phone"],
                      data["course"], data["semester"]))
            messagebox.showinfo("Success", "Student added successfully.")
            self.clear_form()
            self.load_students()
        except sqlite3.IntegrityError:
            messagebox.showerror("Duplicate Roll Number",
                                 "This roll number already exists. Please use a unique roll number.")

    def load_students(self, query=""):
        for item in self.tree.get_children():
            self.tree.delete(item)

        with self.connect_db() as conn:
            if query:
                pattern = f"%{query}%"
                rows = conn.execute("""
                    SELECT * FROM students
                    WHERE roll_no LIKE ? OR name LIKE ? OR email LIKE ?
                       OR phone LIKE ? OR course LIKE ? OR semester LIKE ?
                    ORDER BY id DESC
                """, (pattern, pattern, pattern, pattern, pattern, pattern)).fetchall()
            else:
                rows = conn.execute("SELECT * FROM students ORDER BY id DESC").fetchall()

        for row in rows:
            self.tree.insert("", "end", values=row)

        self.status_var.set(f"Total records displayed: {len(rows)}")

    def search_students(self):
        self.load_students(self.search_var.get().strip())

    def show_all_students(self):
        self.search_var.set("")
        self.load_students()

    def on_row_select(self, event=None):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        self.selected_student_id = values[0]

        for key, value in zip(
            ("roll_no", "name", "email", "phone"), values[1:5]
        ):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, value)

        self.course_var.set(values[5])
        self.semester_var.set(values[6])

    def update_student(self):
        if not self.selected_student_id:
            messagebox.showwarning("Select Student", "Please select a student record to update.")
            return
        data = self.get_form_data()
        if not data:
            return
        try:
            with self.connect_db() as conn:
                conn.execute("""
                    UPDATE students
                    SET roll_no=?, name=?, email=?, phone=?, course=?, semester=?
                    WHERE id=?
                """, (data["roll_no"], data["name"], data["email"], data["phone"],
                      data["course"], data["semester"], self.selected_student_id))
            messagebox.showinfo("Success", "Student record updated successfully.")
            self.clear_form()
            self.load_students()
        except sqlite3.IntegrityError:
            messagebox.showerror("Duplicate Roll Number",
                                 "Another student already uses this roll number.")

    def delete_student(self):
        if not self.selected_student_id:
            messagebox.showwarning("Select Student", "Please select a student record to delete.")
            return
        confirm = messagebox.askyesno(
            "Confirm Delete", "Are you sure you want to delete this student record?"
        )
        if confirm:
            with self.connect_db() as conn:
                conn.execute("DELETE FROM students WHERE id=?",
                             (self.selected_student_id,))
            messagebox.showinfo("Deleted", "Student record deleted successfully.")
            self.clear_form()
            self.load_students()

    def clear_form(self):
        for widget in self.entries.values():
            widget.delete(0, tk.END)
        self.course_var.set("")
        self.semester_var.set("")
        self.selected_student_id = None
        for item in self.tree.selection():
            self.tree.selection_remove(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
