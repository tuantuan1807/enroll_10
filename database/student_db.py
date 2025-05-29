import hashlib
from database.init_db import Database
from model.student import Student

class StudentDatabase:
    def __init__(self):
        self.db = Database()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def registerStudent(self, uname, pwd, fname, birth, gender, school):
        hashed_pwd = self.hash_password(pwd)
        sql = """
            INSERT INTO student (uname, pwd, fname, birth, gender, school)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            self.db.execute(sql, (uname, hashed_pwd, fname, birth, gender, school))
            return True
        except Exception:
            return False

    def fetchAllStudents(self):
        sql = """SELECT  * FROM student"""
        rows = self.db.fetchall(sql)
        return [Student(*row) for row in rows]
    def fetchAllStudentsManage(self):
        school_dict = {}
        rows_school = self.db.fetchall("SELECT id, name FROM school")
        for row in rows_school:
            school_dict[row[0]] = row[1]
        sql = "SELECT * FROM student"
        rows = self.db.fetchall(sql)
        result = []
        from model.student import Student
        for row in rows:
            student = Student(*row[:14])
            nv1_id = student.first_choice
            nv2_id = student.second_choice
            nv1_name = school_dict.get(nv1_id, "") if nv1_id else ""
            nv2_name = school_dict.get(nv2_id, "") if nv2_id else ""
            result.append((student, nv1_name, nv2_name))
        return result
    def deleteStudent(self, student_id):
        sql = "DELETE FROM student WHERE id=?"
        try:
            self.db.execute(sql, (student_id,))
            return True
        except Exception:
            return False

    def check_uname_exists(self, uname):
        sql = "SELECT * FROM student WHERE uname=?"
        return self.db.fetchone(sql, (uname,)) is not None
    def deleteStudent(self, student_id):
        sql = "DELETE FROM student WHERE id=?"
        try:
            self.db.execute(sql, (student_id,))
            return True
        except Exception:
            return False
    def update_scores(self, student_id, math, literature, english):
        sql = "UPDATE student SET math_score=?, literature_score=?, english_score=? WHERE id=?"
        try:
            self.db.execute(sql, (math, literature, english, student_id))
            return True
        except Exception:
            return False
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    def login(self, username, password):
        hashed_pwd = self.hash_password(password)
        sql = "SELECT id, uname, pwd, fname, birth, gender, school, math_score, literature_score, english_score, first_choice, second_choice, exam_room_id, result FROM student WHERE uname=? AND pwd=?"
        row = self.db.fetchone(sql, (username, hashed_pwd))
        if row:
            from model.student import Student
            return Student(*row)
        return None
    def update_wish(self, student_id, nv1_id, nv2_id):
        sql = "UPDATE student SET first_choice=?, second_choice=? WHERE id=?"
        try:
            self.db.execute(sql, (nv1_id, nv2_id, student_id))
            return True
        except Exception:
            return False
    def update_info(self, student_id, fname, birth, gender, school):
            sql = "UPDATE student SET fname=?, birth=?, gender=?, school=? WHERE id=?"
            try:
                self.db.execute(sql, (fname, birth, gender, school, student_id))
                return True
            except Exception:
                return False
    def update_info_with_pwd(self, student_id, fname, birth, gender, school, new_pwd):
        hashed_pwd = hashlib.sha256(new_pwd.encode()).hexdigest()
        sql = "UPDATE student SET fname=?, birth=?, gender=?, school=?, pwd=? WHERE id=?"
        try:
            self.db.execute(sql, (fname, birth, gender, school, hashed_pwd, student_id))
            return True
        except Exception:
            return False
        from view.manage.view_exam_list import ViewExamListWindow
    def get_students_by_room(self, room_id):
        sql = "SELECT id, uname, pwd, fname, birth, gender, school, math_score, literature_score, english_score, first_choice, second_choice, exam_room_id, result FROM student WHERE exam_room_id=?"
        rows = self.db.fetchall(sql, (room_id,))
        return [Student(*row) for row in rows]