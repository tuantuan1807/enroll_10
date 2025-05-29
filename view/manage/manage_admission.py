import tkinter as tk
from tkinter import ttk, messagebox
from controller.admission_controller import AdmissionController
from controller.school_controller import SchoolController
# ... các import và class giữ nguyên ...

class ManageAdmission(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Xét tuyển & Danh sách trúng tuyển")
        self.geometry("1000x500")
        self.controller = AdmissionController()
        self.school_controller = SchoolController()

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Xét tuyển", command=self.admission).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Reset", command=self.reset_admission).pack(side=tk.LEFT, padx=5)

        schools = self.school_controller.get_all_schools()
        self.school_map = {s.name: s.id for s in schools}
        self.school_var = tk.StringVar()
        self.combo_school = ttk.Combobox(self, values=list(self.school_map.keys()), textvariable=self.school_var, state="readonly")
        self.combo_school.pack(pady=5)
        self.combo_school.bind("<<ComboboxSelected>>", self.show_admitted_students)

        # Thêm các cột trường, NV1, NV2
        columns = ("id", "fname", "school", "first_choice", "second_choice", "math", "literature", "english")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=20)
        for col, text in zip(columns, ["ID", "Họ tên", "Trường", "NV1", "NV2", "Toán", "Văn", "Anh"]):
            self.tree.heading(col, text=text)
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def admission(self):
        if self.controller.admission():
            messagebox.showinfo("Thành công", "Đã xét tuyển!")
            self.show_admitted_students()
        else:
            messagebox.showerror("Lỗi", "Xét tuyển thất bại.")

    def reset_admission(self):
        if self.controller.reset_admission():
            messagebox.showinfo("Thành công", "Đã reset kết quả xét tuyển!")
            self.show_admitted_students()
        else:
            messagebox.showerror("Lỗi", "Reset thất bại.")

    def show_admitted_students(self, event=None):
        for row in self.tree.get_children():
            self.tree.delete(row)
        school_name = self.school_var.get()
        if not school_name:
            return
        school_id = self.school_map[school_name]

        students = self.controller.get_admitted_students_by_school(school_id)
        for s in students:
            self.tree.insert("", "end", values=s)