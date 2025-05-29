from tkinter import Tk, Label, Entry, Button, messagebox
from view.manage.login import AdminLoginWindow
from view.student.login import StudentLoginWindow
if __name__ == "__main__":
    # app = AdminLoginWindow()
    app = StudentLoginWindow()
    app.mainloop()