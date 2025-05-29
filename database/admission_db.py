from database.init_db import Database

class AdmissionDatabase:
    def __init__(self):
        self.db = Database()
    def admission(self):
        self.db.execute("UPDATE student SET result=NULL")
        schools = self.db.fetchall("SELECT id, score, quantity FROM school")
    
    
        for school_id, score, quantity in schools:
            students = self.db.fetchall("""
                SELECT id, math_score+literature_score+english_score AS total
                FROM student
                WHERE first_choice=? AND result IS NULL AND (math_score+literature_score+english_score)>=?
                ORDER BY total DESC
            """, (school_id, score))
    
            admitted = []
            cutoff_score = None
            for idx, (student_id, total) in enumerate(students):
                if idx < quantity:
                    admitted.append((student_id, total))
                    cutoff_score = total
                elif cutoff_score is not None and total == cutoff_score:
                    admitted.append((student_id, total))
                else:
                    break
    
            for student_id, _ in admitted:
                self.db.execute("UPDATE student SET result=? WHERE id=?", (school_id, student_id))
    
      
        for school_id, score, quantity in schools:
            admitted_count = self.db.fetchall("SELECT COUNT(*) FROM student WHERE result=?", (school_id,))[0][0]
            remain = quantity - admitted_count
            if remain > 0:
                students_nv2 = self.db.fetchall("""
                    SELECT id, math_score+literature_score+english_score AS total
                    FROM student
                    WHERE second_choice=? AND result IS NULL AND (math_score+literature_score+english_score)>=?
                    ORDER BY total DESC
                """, (school_id, score))
    
                admitted_nv2 = []
                cutoff_score_nv2 = None
                for idx, (student_id, total) in enumerate(students_nv2):
                    if idx < remain:
                        admitted_nv2.append((student_id, total))
                        cutoff_score_nv2 = total
                    elif cutoff_score_nv2 is not None and total == cutoff_score_nv2:
                        admitted_nv2.append((student_id, total))
                    else:
                        break
    
                for student_id, _ in admitted_nv2:
                    self.db.execute("UPDATE student SET result=? WHERE id=?", (school_id, student_id))
        self.db.commit()
        return True



    def get_admitted_students_by_school(self, school_id):
        school_dict = {}
        rows_school = self.db.fetchall("SELECT id, name FROM school")
        for row in rows_school:
            school_dict[row[0]] = row[1]
    
        sql = """
            SELECT id, fname, school, first_choice, second_choice,
                   math_score, literature_score, english_score
            FROM student
            WHERE result = ?
            ORDER BY math_score + literature_score + english_score DESC
        """
        rows = self.db.fetchall(sql, (school_id,))
        result = []
        for row in rows:
            nv1_name = school_dict.get(row[3], "") if row[3] else ""
            nv2_name = school_dict.get(row[4], "") if row[4] else ""
            # row: id, fname, school, first_choice, second_choice, math, lit, eng
            result.append((
                row[0], row[1], row[2], nv1_name, nv2_name, row[5], row[6], row[7]
            ))
        return result
    def reset_admission(self):
        try:
            self.db.execute("UPDATE student SET result=NULL")
            return True
        except Exception:
            return False