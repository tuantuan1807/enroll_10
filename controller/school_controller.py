from database.school_db import SchoolDatabase
class SchoolController:
    def __init__(self):
        self.db = SchoolDatabase()
    def add_school(self, name, quantity, score):
        return self.db.add_school(name, quantity, score)
    def delete_school(self, school_id):
        return self.db.delete_school(school_id)
    def get_all_schools(self):
        return self.db.get_all_schools()  
    def get_school_name_by_id(self, school_id):
        return self.db.get_school_name_by_id(school_id)
    # def update_school(self, school_id, quantity, score):
    #     return self.db.update_school(school_id, quantity, score)
    def update_school(self, school_id, quantity, score, name):
        return self.db.update_school(school_id, quantity, score, name)
    def get_school_id_by_name(self, name):
        return self.db.get_school_id_by_name(name)