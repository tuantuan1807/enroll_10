import hashlib
from database.init_db import Database

class AdminDatabase:
    def __init__(self):
        self.db = Database()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_login(self, username, password):
        hashed_pwd = self.hash_password(password)
        sql = "SELECT * FROM admin WHERE uname=? AND pwd=?"
        return self.db.fetchone(sql, (username, hashed_pwd))

    def close(self):
        self.db.close()