class Student:
    def __init__(self, id, uname, pwd, fname, birth, gender, school,
                 math_score=0, literature_score=0, english_score=0,
                 first_choice=None, second_choice=None, exam_room_id=None, result=None):
        self.id = id
        self.uname = uname
        self.pwd = pwd
        self.fname = fname
        self.birth = birth
        self.gender = gender
        self.school = school
        self.math_score = math_score
        self.literature_score = literature_score
        self.english_score = english_score
        self.first_choice = first_choice
        self.second_choice = second_choice
        self.exam_room_id = exam_room_id
        self.result = result