from database.admin_db import AdminDatabase

class AdminController:
    def __init__(self):
        self.db = AdminDatabase()

    def login(self, username, password):
        return self.db.check_login(username, password)

    def close(self):
        self.db.close()