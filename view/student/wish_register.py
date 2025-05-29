import tkinter as tk
from tkinter import ttk, messagebox
from controller.school_controller import SchoolController
from controller.student_controller import StudentController

class RegisterWishWindow(tk.Toplevel):
    def __init__(self, student, parent=None):
        super().__init__(parent)
        self.student = student
        self.title("Đăng ký nguyện vọng")
        self.geometry("400x250")
        self.school_controller = SchoolController()
        self.student_controller = StudentController()

        if self.student.first_choice or self.student.second_choice:
            tk.Label(self, text="Bạn đã đăng ký nguyện vọng, không thể sửa!", fg="red", font=("Arial", 12, "bold")).pack(pady=30)
            tk.Button(self, text="Đóng", command=self.destroy).pack(pady=10)
            return

        tk.Label(self, text="Chọn nguyện vọng 1:").pack(pady=5)
        schools = self.school_controller.get_all_schools()
        self.school_map = {s.name: s.id for s in schools}
        self.nv1_var = tk.StringVar()
        self.nv1_combo = ttk.Combobox(self, values=list(self.school_map.keys()), textvariable=self.nv1_var, state="readonly")
        self.nv1_combo.pack(pady=5)

        tk.Label(self, text="Chọn nguyện vọng 2:").pack(pady=5)
        self.nv2_var = tk.StringVar()
        self.nv2_combo = ttk.Combobox(self, values=list(self.school_map.keys()), textvariable=self.nv2_var, state="readonly")
        self.nv2_combo.pack(pady=5)

        tk.Button(self, text="Đăng ký", command=self.register).pack(pady=15)

    def register(self):
        nv1 = self.nv1_var.get()
        nv2 = self.nv2_var.get()
        if not nv1 or not nv2:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn đủ 2 nguyện vọng.")
            return
        if nv1 == nv2:
            messagebox.showwarning("Trùng nguyện vọng", "Nguyện vọng 1 và 2 phải khác nhau.")
            return
        nv1_id = self.school_map[nv1]
        nv2_id = self.school_map[nv2]
        if self.student_controller.update_wish(self.student.id, nv1_id, nv2_id):
            messagebox.showinfo("Thành công", "Đăng ký nguyện vọng thành công!")
            self.destroy()
        else:
            messagebox.showerror("Lỗi", "Đăng ký thất bại.")