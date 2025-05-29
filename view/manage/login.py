import tkinter as tk
from tkinter import messagebox
from controller.admin_controller import AdminController
from view.manage.main_manage import MainManageWindow  
class AdminLoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Đăng nhập quản trị viên")
        self.geometry("320x200")
        self.controller = AdminController()

        tk.Label(self, text="Đăng nhập quản trị viên", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self, text="Tên đăng nhập:").pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)

        tk.Label(self, text="Mật khẩu:").pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        tk.Button(self, text="Đăng nhập", command=self.login).pack(pady=15)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        admin = self.controller.login(username, password)
        if admin:
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
            self.withdraw() 
            admin_info = {'fname': admin[3]} if isinstance(admin, tuple) else admin
            MainManageWindow(admin_info, root=self)
        else:
            messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu.")