import tkinter as tk
from tkinter import messagebox
from controller.school_controller import SchoolController

class AdmissionResultWindow(tk.Toplevel):
    def __init__(self, student, parent=None):
        super().__init__(parent)
        self.title("Kết quả trúng tuyển")
        self.geometry("350x180")
        self.school_controller = SchoolController()

        if student.result:
            school_name = self.school_controller.get_school_name_by_id(student.result)
            tk.Label(self, text="Chúc mừng bạn đã trúng tuyển!", font=("Arial", 13, "bold"), fg="green").pack(pady=10)
            tk.Label(self, text=f"Trường trúng tuyển: {school_name}", font=("Arial", 12)).pack(pady=10)
        else:
            tk.Label(self, text="Bạn đã rớt kỳ thi.", font=("Arial", 12)).pack(pady=30)

        tk.Button(self, text="Đóng", command=self.destroy).pack(pady=10)