from database.student_db import StudentDatabase
import hashlib
class StudentController:
    def __init__(self):
        self.db = StudentDatabase()

    def register_student(self, uname, pwd, fname, birth, gender, school):
        return self.db.registerStudent(uname, pwd, fname, birth, gender, school)

    def fetch_all_students(self):
        return self.db.fetchAllStudents() 
    def fetchAllStudentsManage(self):
        return self.db.fetchAllStudentsManage() 
    def delete_student(self, student_id):
        return self.db.deleteStudent(student_id)

    def check_uname_exists(self, uname):
        return self.db.check_uname_exists(uname)
    def delete_student(self, student_id):
        return self.db.deleteStudent(student_id)
    def update_scores(self, student_id, math, literature, english):
        return self.db.update_scores(student_id, math, literature, english)
    def login(self, username, password):
        return self.db.login(username, password)
    def update_wish(self, student_id, nv1_id, nv2_id):
        return self.db.update_wish(student_id, nv1_id, nv2_id)
    def update_info(self, student_id, fname, birth, gender, school):
        return self.db.update_info(student_id, fname, birth, gender, school)
    def update_info_with_pwd(self, student_id, fname, birth, gender, school, new_pwd):
        return self.db.update_info_with_pwd(student_id, fname, birth, gender, school, new_pwd)
    def get_students_by_room(self, room_id):
        return self.db.get_students_by_room(room_id)