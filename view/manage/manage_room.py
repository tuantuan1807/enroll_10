import tkinter as tk
from tkinter import ttk, messagebox
from controller.room_controller import RoomController
from controller.school_controller import SchoolController
from controller.student_controller import StudentController

class ManageRoom(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Quản lý phòng thi")
        self.geometry("850x500")
        self.room_controller = RoomController()
        self.school_controller = SchoolController()
        self.student_controller = StudentController()

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Tên phòng:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(form)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Trường:").grid(row=0, column=2, padx=5, pady=5)
        self.school_names = [s.name for s in self.school_controller.get_all_schools()]
        self.school_var = tk.StringVar()
        self.combo_school = ttk.Combobox(form, values=self.school_names, textvariable=self.school_var, state="readonly")
        self.combo_school.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form, text="Sức chứa:").grid(row=0, column=4, padx=5, pady=5)
        self.entry_capacity = tk.Entry(form)
        self.entry_capacity.grid(row=0, column=5, padx=5, pady=5)

        tk.Button(form, text="Thêm phòng", command=self.add_room).grid(row=0, column=6, padx=5, pady=5)
        tk.Button(form, text="Sửa phòng", command=self.edit_room).grid(row=0, column=7, padx=5, pady=5)
        tk.Button(form, text="Xóa phòng", command=self.delete_room).grid(row=0, column=8, padx=5, pady=5)

       
        columns = ("id", "name", "school", "capacity")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)
        for col, text in zip(columns, ["ID", "Tên phòng", "Trường", "Sức chứa"]):
            self.tree.heading(col, text=text)
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

       
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Sắp xếp phân phòng", command=self.assign_rooms).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Reset phân phòng", command=self.reset_assignments).pack(side=tk.LEFT, padx=10)

        self.selected_room_id = None
        self.refresh_room_list()

    def refresh_room_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        rooms = self.room_controller.get_all_rooms()
        for room in rooms:
            school_name = self.school_controller.get_school_name_by_id(room[2])  
            self.tree.insert("", "end", values=(room[0], room[1], school_name, room[3]))
    def add_room(self):
        name = self.entry_name.get().strip()
        school_name = self.combo_school.get()
        capacity = self.entry_capacity.get().strip()
        if not name or not school_name or not capacity.isdigit():
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ và đúng thông tin.")
            return
        school_id = self.school_controller.get_school_id_by_name(school_name)
        if self.room_controller.add_room(name, school_id, int(capacity)):
            messagebox.showinfo("Thành công", "Đã thêm phòng thi.")
            self.refresh_room_list()
        else:
            messagebox.showerror("Lỗi", "Không thể thêm phòng.")

    def edit_room(self):
        if not self.selected_room_id:
            messagebox.showwarning("Chọn phòng", "Vui lòng chọn phòng để sửa.")
            return
        name = self.entry_name.get().strip()
        school_name = self.combo_school.get()
        capacity = self.entry_capacity.get().strip()
        if not name or not school_name or not capacity.isdigit():
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ và đúng thông tin.")
            return
        school_id = self.school_controller.get_school_id_by_name(school_name)
        if self.room_controller.edit_room(self.selected_room_id, name, school_id, int(capacity)):
            messagebox.showinfo("Thành công", "Đã sửa phòng thi.")
            self.refresh_room_list()
        else:
            messagebox.showerror("Lỗi", "Không thể sửa phòng.")

    def delete_room(self):
        if not self.selected_room_id:
            messagebox.showwarning("Chọn phòng", "Vui lòng chọn phòng để xóa.")
            return
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa phòng này?"):
            if self.room_controller.delete_room(self.selected_room_id):
                messagebox.showinfo("Thành công", "Đã xóa phòng thi.")
                self.refresh_room_list()
            else:
                messagebox.showerror("Lỗi", "Không thể xóa phòng.")

    def on_tree_select(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        values = self.tree.item(selected, "values")
        self.selected_room_id = int(values[0])
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, values[1])
        self.combo_school.set(values[2])
        self.entry_capacity.delete(0, tk.END)
        self.entry_capacity.insert(0, values[3])

    def assign_rooms(self):
       
        if self.room_controller.assign_rooms():
            messagebox.showinfo("Thành công", "Đã sắp xếp phân phòng cho thí sinh.")
        else:
            messagebox.showerror("Lỗi", "Không thể phân phòng.")

    def reset_assignments(self):
        if self.room_controller.reset_assignments():
            messagebox.showinfo("Thành công", "Đã reset phân phòng.")
        else:
            messagebox.showerror("Lỗi", "Không thể reset phân phòng.")