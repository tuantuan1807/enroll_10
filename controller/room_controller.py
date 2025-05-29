class RoomController:
    def __init__(self):
        from database.room_db import RoomDatabase
        self.db = RoomDatabase()

    def get_all_rooms(self):
        return self.db.get_all_rooms()

    def add_room(self, name, school_id, capacity):
        return self.db.add_room(name, school_id, capacity)

    def edit_room(self, room_id, name, school_id, capacity):
        return self.db.edit_room(room_id, name, school_id, capacity)

    def delete_room(self, room_id):
        return self.db.delete_room(room_id)

    def assign_rooms(self):
        return self.db.assign_rooms()

    def reset_assignments(self):
        return self.db.reset_assignments()
    def get_rooms_by_school(self, school_id):
        return self.db.get_rooms_by_school(school_id)
    def get_room_by_id(self, room_id):
        return self.db.get_room_by_id(room_id)