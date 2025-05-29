import tkinter as tk
from tkinter import messagebox
from controller.room_controller import RoomController
from controller.school_controller import SchoolController

class ExamLocationWindow(tk.Toplevel):
    def __init__(self, student, parent=None):
        super().__init__(parent)
        self.title("Địa điểm thi của bạn")
        self.geometry("350x180")
        self.room_controller = RoomController()
        self.school_controller = SchoolController()

        if not student.exam_room_id:
            tk.Label(self, text="Bạn chưa được xếp phòng thi.", font=("Arial", 12), fg="red").pack(pady=30)
        else:
            room = self.room_controller.get_room_by_id(student.exam_room_id)
            if room:
                room_name = room['name']
                school_name = self.school_controller.get_school_name_by_id(room['school_id'])
                tk.Label(self, text="ĐỊA ĐIỂM THI", font=("Arial", 13, "bold"), fg="blue").pack(pady=10)
                tk.Label(self, text=f"Phòng thi: {room_name}", font=("Arial", 12)).pack(pady=5)
                tk.Label(self, text=f"Trường thi: {school_name}", font=("Arial", 12)).pack(pady=5)
            else:
                tk.Label(self, text="Không tìm thấy thông tin phòng thi.", font=("Arial", 12), fg="red").pack(pady=30)

        tk.Button(self, text="Đóng", command=self.destroy).pack(pady=10)