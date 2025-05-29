import tkinter as tk
from tkinter import messagebox

class ViewScoresWindow(tk.Toplevel):
    def __init__(self, student, parent=None):
        super().__init__(parent)
        self.title("Kết quả thi của bạn")
        self.geometry("350x220")

        tk.Label(self, text="KẾT QUẢ THI", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self, text=f"Họ tên: {student.fname}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self, text=f"Toán: {student.math_score}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self, text=f"Văn: {student.literature_score}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self, text=f"Anh: {student.english_score}", font=("Arial", 12)).pack(pady=5)
        total = round((student.math_score or 0) +(student.literature_score or 0) +(student.english_score or 0),1)
        tk.Label(self, text=f"Tổng điểm: {total}", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Button(self, text="Đóng", command=self.destroy).pack(pady=5)