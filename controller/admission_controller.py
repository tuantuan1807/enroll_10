from database.admission_db import AdmissionDatabase

class AdmissionController:
    def __init__(self):
        self.db = AdmissionDatabase()

    def admission(self):
        return self.db.admission()

    def get_admitted_students_by_school(self, school_id):
        return self.db.get_admitted_students_by_school(school_id)
    def reset_admission(self):
        return self.db.reset_admission()