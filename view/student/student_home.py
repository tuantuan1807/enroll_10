import tkinter as tk
from tkinter import messagebox
from view.student.wish_register import RegisterWishWindow
from view.student.wish_view import UpdateWishWindow
from view.student.score_view import ViewScoresWindow
from view.student.admission_result import AdmissionResultWindow
from view.student.edit_profile import EditInfoWindow
from view.student.exam_location import ExamLocationWindow
class StudentHomeWindow(tk.Toplevel):
    def __init__(self, student, parent=None):
        super().__init__(parent)
        self.student = student
        self.title("Trang chủ thí sinh")
        self.geometry("400x400")

        tk.Label(self, text=f"Xin chào, {self.student.fname}", font=("Arial", 14, "bold")).pack(pady=15)

        tk.Button(self, text="Sửa thông tin cá nhân", width=30, command=self.edit_info).pack(pady=5)
        tk.Button(self, text="Đăng ký nguyện vọng", width=30, command=self.register_wish).pack(pady=5)
        tk.Button(self, text="Xem địa điểm thi", width=30, command=self.view_exam_location).pack(pady=5)
        tk.Button(self, text="Cập nhật nguyện vọng", width=30, command=self.view_wish).pack(pady=5)
        tk.Button(self, text="Xem kết quả thi", width=30, command=self.view_scores).pack(pady=5)
        tk.Button(self, text="Xem kết quả trúng tuyển", width=30, command=self.view_admission_result).pack(pady=5)
        tk.Button(self, text="Đăng xuất", width=30, fg="red", command=self.logout).pack(pady=20)

    def edit_info(self):
        EditInfoWindow(self.student, parent=self)
    def register_wish(self):
        RegisterWishWindow(self.student, parent=self)
    def view_exam_location(self):
        ExamLocationWindow(self.student, parent=self)
    def view_wish(self):
        UpdateWishWindow(self.student, parent=self)
        # messagebox.showinfo("Xem nguyện vọng", "Chức năng Xem nguyện vọng.")
    def view_scores(self):
        ViewScoresWindow(self.student, parent=self)
    def view_admission_result(self):
        AdmissionResultWindow(self.student, parent=self)
    
    def logout(self):
        self.destroy()