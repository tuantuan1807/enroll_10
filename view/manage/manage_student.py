import tkinter as tk
from tkinter import ttk, messagebox
import random
import unicodedata
from controller.student_controller import StudentController

class ManageStudent(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Quản lý thí sinh")
        self.geometry("1000x1000")
        self.controller = StudentController()

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Họ tên:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_fname = tk.Entry(form)
        self.entry_fname.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Ngày sinh:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_birth = tk.Entry(form)
        self.entry_birth.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form, text="Giới tính:").grid(row=1, column=0, padx=5, pady=5)
        self.gender_var = tk.StringVar(value="Nam")
        tk.OptionMenu(form, self.gender_var, "Nam", "Nữ").grid(row=1, column=1, padx=5, pady=5)

        school_names = [
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

        tk.Label(form, text="Trường THCS:").grid(row=1, column=2, padx=5, pady=5)

        self.school_var = tk.StringVar()
        self.entry_school = ttk.Combobox(form, values=school_names, textvariable=self.school_var, state="readonly")
        self.entry_school.grid(row=1, column=3, padx=5, pady=5)

        tk.Button(form, text="Thêm thí sinh", command=self.add_student).grid(row=2, column=0, columnspan=4, pady=10)


        columns = ("stt", "id", "fname", "uname", "school", "first_choice", "second_choice")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)
        for col, text in zip(columns, ["STT", "ID", "Họ tên", "Tên đăng nhập", "Trường THCS", "NV1", "NV2"]):
            self.tree.heading(col, text=text)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Button(self, text="Xóa thí sinh", command=self.delete_student).pack(pady=5)

        self.refresh_student_list()

    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFD', input_str)
        return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

    def generate_unique_uname(self, fname):
        base = self.remove_accents(fname).replace(" ", "").lower()
        for _ in range(50):
            uname = f"{base}{random.randint(10000, 90000)}"
            if not self.controller.check_uname_exists(uname):
                return uname
        raise Exception("Không thể tạo tên đăng nhập duy nhất.")

    def add_student(self):
        fname = self.entry_fname.get().strip()
        birth = self.entry_birth.get().strip()
        gender = self.gender_var.get()
        school = self.entry_school.get().strip()
        if not fname or not birth or not gender or not school:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")
            return
        try:
            uname = self.generate_unique_uname(fname)
            password = "a"
            success = self.controller.register_student(uname, password, fname, birth, gender, school)
            if success:
                messagebox.showinfo("Thành công", "Đã thêm thí sinh mới.")
                self.refresh_student_list()
            else:
                messagebox.showerror("Lỗi", "Không thể thêm thí sinh.")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def refresh_student_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        students = self.controller.fetchAllStudentsManage()
        for idx, (student, nv1_name, nv2_name) in enumerate(students, 1):
            self.tree.insert("", "end", values=(
                idx, student.id, student.fname, student.uname, student.school, nv1_name, nv2_name
            ))

    def delete_student(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Chọn thí sinh", "Vui lòng chọn thí sinh để xóa.")
            return
        values = self.tree.item(selected, "values")
        student_id = values[1]
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa thí sinh này?"):
            if self.controller.delete_student(student_id):
                messagebox.showinfo("Thành công", "Đã xóa thí sinh.")
                self.refresh_student_list()
            else:
                messagebox.showerror("Lỗi", "Không thể xóa thí sinh.")