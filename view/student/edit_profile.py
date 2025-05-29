import tkinter as tk
from tkinter import messagebox, ttk
from controller.student_controller import StudentController
from controller.school_controller import SchoolController

class EditInfoWindow(tk.Toplevel):
    def __init__(self, student, parent=None):
        super().__init__(parent)
        self.student = student
        self.controller = StudentController()
        self.school_controller = SchoolController()
        self.title("Sửa thông tin cá nhân")
        self.geometry("350x370")

        tk.Label(self, text="Sửa thông tin cá nhân", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self, text="Họ tên:").pack()
        self.entry_fname = tk.Entry(self)
        self.entry_fname.insert(0, student.fname)
        self.entry_fname.pack(pady=5)

        tk.Label(self, text="Ngày sinh:").pack()
        self.entry_birth = tk.Entry(self)
        self.entry_birth.insert(0, student.birth)
        self.entry_birth.pack(pady=5)

        tk.Label(self, text="Giới tính:").pack()
        self.gender_var = tk.StringVar(value=student.gender)
        tk.OptionMenu(self, self.gender_var, "Nam", "Nữ").pack(pady=5)

        tk.Label(self, text="Trường THCS:").pack()
        schools = self.school_controller.get_all_schools()
        self.school_names = [
        "Trường THCS Bảo Ninh",
        "Trường THCS Bắc Nghĩa",
        "Trường THCS Hải Thành",
        "Trường THCS Đồng Hải",
        "Trường THCS Lộc Ninh",
        "Trường THCS số 1 Bắc Lý",
        "Trường THCS số 1 Nam Lý",
        "Trường THCS số 1 Đồng Sơn",
        "Trường THCS số 2 Bắc Lý",
        "Trường THCS số 2 Nam Lý",
        "Trường THCS Đức Ninh Đông",
        "Trường THCS Đồng Phú",
        "Trường THCS Đức Ninh",
        "Trường TH&THCS Quang Phú",
        "Trường TH&THCS Thuận Đức",
        "Trường TH&THCS Phú Hải"
    ]
        self.school_var = tk.StringVar(value=student.school)  
        self.combo_school = ttk.Combobox(
            self,
            values=self.school_names,
            textvariable=self.school_var,
            state="readonly"
        )
        self.combo_school.pack(pady=5)

        tk.Label(self, text="Mật khẩu mới (bỏ trống nếu không đổi):").pack()
        self.entry_pwd = tk.Entry(self, show="*")
        self.entry_pwd.pack(pady=5)

        tk.Button(self, text="Lưu", command=self.save).pack(pady=15)

    def save(self):
        fname = self.entry_fname.get().strip()
        birth = self.entry_birth.get().strip()
        gender = self.gender_var.get()
        school = self.school_var.get().strip()
        new_pwd = self.entry_pwd.get().strip()
        if not fname or not birth or not gender or not school:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")
            return

        if not new_pwd:
            result = self.controller.update_info(self.student.id, fname, birth, gender, school)
        else:
            result = self.controller.update_info_with_pwd(self.student.id, fname, birth, gender, school, new_pwd)
        if result:
            messagebox.showinfo("Thành công", "Cập nhật thông tin thành công!")
            self.destroy()
        else:
            messagebox.showerror("Lỗi", "Cập nhật thất bại.")
