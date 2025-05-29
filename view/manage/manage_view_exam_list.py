import tkinter as tk
from tkinter import ttk, messagebox
from controller.room_controller import RoomController
from controller.school_controller import SchoolController
from controller.student_controller import StudentController

class ViewExamListWindow(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Xem danh sách thi theo phòng và trường")
        self.geometry("900x600")
        self.room_controller = RoomController()
        self.school_controller = SchoolController()
        self.student_controller = StudentController()


              
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)
        tk.Label(form_frame, text="Trường THPT:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        schools = self.school_controller.get_all_schools()
        self.school_map = {s.name: s.id for s in schools}
        self.school_var = tk.StringVar()
        self.combo_school = ttk.Combobox(form_frame, values=list(self.school_map.keys()), textvariable=self.school_var, state="readonly")
        self.combo_school.grid(row=0, column=1, padx=5, pady=5)
        self.combo_school.bind("<<ComboboxSelected>>", self.update_rooms)
        tk.Label(form_frame, text="Phòng thi:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.room_var = tk.StringVar()
        self.combo_room = ttk.Combobox(form_frame, values=[], textvariable=self.room_var, state="readonly")
        self.combo_room.grid(row=0, column=3, padx=5, pady=5)
        self.combo_room.bind("<<ComboboxSelected>>", self.show_exam_list)

        columns = ("id", "fname", "birth", "gender", "school")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=20)
        for col, text in zip(columns, ["ID", "Họ tên", "Ngày sinh", "Giới tính", "Trường THCS"]):
            self.tree.heading(col, text=text)
            self.tree.column(col, width=150)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


    def update_rooms(self, event=None):
        school_name = self.school_var.get()
        if not school_name:
            self.combo_room['values'] = []
            return
        school_id = self.school_map[school_name]
        rooms = self.room_controller.get_rooms_by_school(school_id)
        self.room_map = {r[1]: r[0] for r in rooms}  
        self.combo_room['values'] = list(self.room_map.keys())
        self.combo_room.set("")

    def show_exam_list(self, event=None):
        for row in self.tree.get_children():
            self.tree.delete(row)
        room_name = self.room_var.get()
        if not room_name:
            return
        room_id = self.room_map[room_name]
        students = self.student_controller.get_students_by_room(room_id)
        for s in students:
            self.tree.insert("", "end", values=(s.id, s.fname, s.birth, s.gender, s.school))