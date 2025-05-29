from database.init_db import Database
from model.school import School
class SchoolDatabase:
    def __init__(self):
        self.db = Database()
    def update_school(self, school_id, quantity, score, name):
        sql = "UPDATE school SET quantity=?, score=?, name=? WHERE id=?"
        try:
            self.db.execute(sql, (quantity, score, name, school_id))
            return True
        except Exception:
            return False
    def get_all_schools(self):
        sql = "SELECT id, name, score, quantity FROM school"
        rows = self.db.fetchall(sql)
        return [School(*row) for row in rows]

    def get_school_name_by_id(self, school_id):
        sql = "SELECT name FROM school WHERE id=?"
        row = self.db.fetchone(sql, (school_id,))
        return row[0] if row else None

    def get_school_id_by_name(self, name):
        sql = "SELECT id FROM school WHERE name=?"
        row = self.db.fetchone(sql, (name,))
        return row[0] if row else None
    def add_school(self, name, quantity, score):
        sql = "INSERT INTO school (name, quantity, score) VALUES (?, ?, ?)"
        try:
            self.db.execute(sql, (name, quantity, score))
            return True
        except Exception:
            return False

    def delete_school(self, school_id):
        sql = "DELETE FROM school WHERE id=?"
        try:
            self.db.execute(sql, (school_id,))
            return True
        except Exception:
            return False
