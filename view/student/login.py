import tkinter as tk
from tkinter import messagebox
from controller.student_controller import StudentController
from view.student.student_home import StudentHomeWindow
class StudentLoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Đăng nhập thí sinh")
        self.geometry("320x200")
        self.controller = StudentController()

        tk.Label(self, text="Đăng nhập thí sinh", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self, text="Tên đăng nhập:").pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)

        tk.Label(self, text="Mật khẩu:").pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        tk.Button(self, text="Đăng nhập", command=self.login).pack(pady=15)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        student = self.controller.login(username, password)
        if student:
            self.withdraw()
            StudentHomeWindow(student, parent=self)
            # messagebox.showinfo("Thành công", f"Chào mừng {student.fname}!")
            
        else:
            messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu.")
