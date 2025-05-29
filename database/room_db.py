from database.init_db import Database

class RoomDatabase:
    def __init__(self):
        self.db = Database()

    def get_all_rooms(self):
        sql = "SELECT id, name, school_id, capacity FROM room"
        rows = self.db.fetchall(sql)
        return rows

    def add_room(self, name, school_id, capacity):
        sql = "INSERT INTO room (name, school_id, capacity) VALUES (?, ?, ?)"
        try:
            self.db.execute(sql, (name, school_id, capacity))
            return True
        except Exception:
            return False

    def edit_room(self, room_id, name, school_id, capacity):
        sql = "UPDATE room SET name=?, school_id=?, capacity=? WHERE id=?"
        try:
            self.db.execute(sql, (name, school_id, capacity, room_id))
            return True
        except Exception:
            return False

    def delete_room(self, room_id):
        sql = "DELETE FROM room WHERE id=?"
        try:
            self.db.execute(sql, (room_id,))
            return True
        except Exception:
            return False

    def assign_rooms(self):
 
        rooms_by_school = {}
        for room in self.db.fetchall("SELECT id, school_id, capacity FROM room"):
            rooms_by_school.setdefault(room[1], []).append({'id': room[0], 'capacity': room[2], 'assigned': 0})

        students = self.db.fetchall("SELECT id, first_choice FROM student WHERE exam_room_id IS NULL")
        for student_id, first_choice in students:
            assigned = False
          
            if first_choice in rooms_by_school:
                for room in rooms_by_school[first_choice]:
                    if room['assigned'] < room['capacity']:
                        self.db.execute("UPDATE student SET exam_room_id=? WHERE id=?", (room['id'], student_id))
                        room['assigned'] += 1
                        assigned = True
                        break
            if not assigned:
                for school_id, room_list in rooms_by_school.items():
                    for room in room_list:
                        if room['assigned'] < room['capacity']:
                            self.db.execute("UPDATE student SET exam_room_id=? WHERE id=?", (room['id'], student_id))
                            room['assigned'] += 1
                            assigned = True
                            break
                    if assigned:
                        break
        return True

    def reset_assignments(self):
        try:
            self.db.execute("UPDATE student SET exam_room_id=NULL")
            return True
        except Exception:
            return False
    def get_rooms_by_school(self, school_id):
        sql = "SELECT id, name FROM room WHERE school_id=?"
        return self.db.fetchall(sql, (school_id,))
    def get_room_by_id(self, room_id):
        sql = "SELECT id, name, school_id, capacity FROM room WHERE id=?"
        row = self.db.fetchone(sql, (room_id,))
        if row:
            return {'id': row[0], 'name': row[1], 'school_id': row[2], 'capacity': row[3]}
        return None