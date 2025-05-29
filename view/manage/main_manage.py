import tkinter as tk
from tkinter import messagebox
from controller.admin_controller import AdminController
from view.manage.manage_student import ManageStudent
from view.manage.manage_room import ManageRoom
from view.manage.manage_score import ManageScore
from view.manage.manage_admission import ManageAdmission
from view.manage.manage_report import ReportWindow
from view.manage.manage_view_exam_list import ViewExamListWindow
from view.manage.manage_school import ManageSchoolWindow
class MainManageWindow(tk.Toplevel):
    def __init__(self, admin_info, root=None):
        super().__init__(root)
        self.title("Trang chủ Quản trị viên")
        self.geometry("400x450")
        self.admin_info = admin_info


        tk.Label(self, text=f"Xin chào, {self.admin_info['fname']}", font=("Arial", 14, "bold")).pack(pady=15)


        tk.Button(self, text="Quản lý thí sinh", width=30, command=self.manage_students).pack(pady=5)
        tk.Button(self, text="Quản lý trường thi", width=30, command=self.manage_school).pack(pady=5)
        tk.Button(self, text="Quản lý phòng thi", width=30, command=self.manage_rooms).pack(pady=5)
        tk.Button(self, text="Xem danh sách thi", width=30, command=self.view_exam_list).pack(pady=5)

        tk.Button(self, text="Nhập điểm", width=30, command=self.input_scores).pack(pady=5)
        tk.Button(self, text="Xét tuyển", width=30, command=self.admission).pack(pady=5)
        tk.Button(self, text="Thống kê & Báo cáo", width=30, command=self.report).pack(pady=5)
        tk.Button(self, text="Đăng xuất", width=30, fg="red", command=self.logout).pack(pady=20)

    
    def manage_students(self):
        ManageStudent(self)
    def manage_school(self):
        ManageSchoolWindow(self)
    def manage_rooms(self):
        ManageRoom(self)
        
    def view_exam_list(self):
         ViewExamListWindow(self)

    def input_scores(self):
        ManageScore(self)
    
    def admission(self):
        ManageAdmission(self)
        # messagebox.showinfo("Xét tuyển", "Chức năng Xét tuyển.")

    def report(self):
        ReportWindow(self)
        # messagebox.showinfo("Thống kê & Báo cáo", "Chức năng Thống kê & Báo cáo.")

    def logout(self):
        self.destroy()