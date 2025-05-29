import tkinter as tk
from tkinter import ttk, messagebox
from controller.student_controller import StudentController

class ManageScore(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Nhập điểm thi")
        self.geometry("900x500")
        self.controller = StudentController()

        columns = ("id", "fname", "school", "math_score", "literature_score", "english_score")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=20)
        for col, text in zip(columns, ["ID", "Họ tên", "Trường", "Toán", "Văn", "Anh"]):
            self.tree.heading(col, text=text)
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree.bind("<Double-1>", self.on_double_click)

        self.editing_entry = None
        self.editing_row = None
        self.editing_col_index = None

        tk.Button(self, text="Lưu điểm", command=self.save_scores).pack(pady=10)

        self.refresh_student_list()

    def refresh_student_list(self):
        
        if self.editing_entry:
            self.editing_entry.destroy()
            self.editing_entry = None
            self.editing_row = None
            self.editing_col_index = None

        for row in self.tree.get_children():
            self.tree.delete(row)
        students = self.controller.fetch_all_students()
        for s in students:
            self.tree.insert("", "end", values=(
                s.id, s.fname, s.school, s.math_score, s.literature_score, s.english_score
            ))

    def on_double_click(self, event):
        region = self.tree.identify("region", event.x, event.y)
        if region != "cell":
            return
        row_id = self.tree.identify_row(event.y)
        col = self.tree.identify_column(event.x)
        col_index = int(col.replace("#", "")) - 1

        if col_index < 3:
            return

        # Nếu đang có ô nhập khác chưa đóng thì đóng nó trước
        if self.editing_entry:
            self.finish_editing()

        x, y, width, height = self.tree.bbox(row_id, col)
        value = self.tree.set(row_id, self.tree["columns"][col_index])

        self.editing_entry = tk.Entry(self.tree)
        self.editing_entry.place(x=x, y=y, width=width, height=height)
        self.editing_entry.insert(0, value)
        self.editing_entry.focus()

        self.editing_entry.bind("<Return>", lambda e: self.finish_editing())
        self.editing_entry.bind("<FocusOut>", lambda e: self.finish_editing())

        self.editing_row = row_id
        self.editing_col_index = col_index

    def finish_editing(self):
        if not self.editing_entry:
            return
        new_value = self.editing_entry.get().strip()
   
        try:
            float(new_value)
        except ValueError:
            messagebox.showerror("Lỗi", "Điểm phải là số!")
            # Không cập nhật, chỉ xóa entry và giữ giá trị cũ
            self.editing_entry.destroy()
            self.editing_entry = None
            self.editing_row = None
            self.editing_col_index = None
            return

      
        col_name = self.tree["columns"][self.editing_col_index]
        self.tree.set(self.editing_row, col_name, new_value)

        self.editing_entry.destroy()
        self.editing_entry = None
        self.editing_row = None
        self.editing_col_index = None

    def save_scores(self):

        if self.editing_entry:
            self.finish_editing()

        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            student_id = values[0]
            try:
                math = float(values[3])
                literature = float(values[4])
                english = float(values[5])
            except ValueError:
                messagebox.showerror("Lỗi", f"Điểm không hợp lệ cho thí sinh ID {student_id}")
                return
            self.controller.update_scores(student_id, math, literature, english)
        messagebox.showinfo("Thành công", "Đã lưu điểm cho tất cả thí sinh.")
        self.refresh_student_list()
