import tkinter as tk
from tkinter import ttk, messagebox
from controller.school_controller import SchoolController

class ManageSchoolWindow(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Quản lý trường THPT")
        self.geometry("700x480")
        self.controller = SchoolController()

    
        form = tk.Frame(self)
        form.pack(pady=10)
        tk.Label(form, text="Tên trường:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(form, width=30)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(form, text="Chỉ tiêu:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_quantity = tk.Entry(form, width=10)
        self.entry_quantity.grid(row=0, column=3, padx=5, pady=5)
        tk.Label(form, text="Điểm chuẩn:").grid(row=0, column=4, padx=5, pady=5)
        self.entry_score = tk.Entry(form, width=10)
        self.entry_score.grid(row=0, column=5, padx=5, pady=5)

        tk.Button(form, text="Thêm mới", command=self.add_school).grid(row=1, column=1, pady=8)
        tk.Button(form, text="Cập nhật", command=self.update_school).grid(row=1, column=3, pady=8)
        tk.Button(form, text="Xóa", command=self.delete_school).grid(row=1, column=5, pady=8)


        columns = ("id", "name", "quantity", "score")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)
        for col, text in zip(columns, ["ID", "Tên trường", "Chỉ tiêu", "Điểm chuẩn"]):
            self.tree.heading(col, text=text)
            self.tree.column(col, width=150)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.refresh()

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        schools = self.controller.get_all_schools()
        for s in schools:
            self.tree.insert("", "end", values=(s.id, s.name, s.quantity, s.score))
        self.clear_form()

    def clear_form(self):
        self.entry_name.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)
        self.entry_score.delete(0, tk.END)
        self.selected_id = None

    def on_select(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        values = self.tree.item(selected, "values")
        self.selected_id = values[0]
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, values[1])
        self.entry_quantity.delete(0, tk.END)
        self.entry_quantity.insert(0, values[2])
        self.entry_score.delete(0, tk.END)
        self.entry_score.insert(0, values[3])

    def add_school(self):
        name = self.entry_name.get().strip()
        quantity = self.entry_quantity.get().strip()
        score = self.entry_score.get().strip()
        if not name or not quantity or not score:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")
            return
        try:
            quantity = int(quantity)
            score = float(score)
        except Exception:
            messagebox.showerror("Lỗi", "Chỉ tiêu phải là số nguyên, điểm chuẩn là số thực.")
            return
        if self.controller.add_school(name, quantity, score):
            messagebox.showinfo("Thành công", "Đã thêm trường mới!")
            self.refresh()
        else:
            messagebox.showerror("Lỗi", "Thêm trường thất bại.")

    def update_school(self):
        if not hasattr(self, "selected_id") or not self.selected_id:
            messagebox.showwarning("Chọn trường", "Vui lòng chọn trường để cập nhật.")
            return
        name = self.entry_name.get().strip()
        quantity = self.entry_quantity.get().strip()
        score = self.entry_score.get().strip()
        if not name or not quantity or not score:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")
            return
        try:
            quantity = int(quantity)
            score = float(score)
        except Exception:
            messagebox.showerror("Lỗi", "Chỉ tiêu phải là số nguyên, điểm chuẩn là số thực.")
            return
        if self.controller.update_school(self.selected_id, quantity, score, name):
            messagebox.showinfo("Thành công", "Cập nhật thành công!")
            self.refresh()
        else:
            messagebox.showerror("Lỗi", "Cập nhật thất bại.")

    def delete_school(self):
        if not hasattr(self, "selected_id") or not self.selected_id:
            messagebox.showwarning("Chọn trường", "Vui lòng chọn trường để xóa.")
            return
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa trường này?"):
            if self.controller.delete_school(self.selected_id):
                messagebox.showinfo("Thành công", "Đã xóa trường.")
                self.refresh()
            else:
                messagebox.showerror("Lỗi", "Không thể xóa trường.")