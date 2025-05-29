import random
import hashlib
from database.init_db import Database
import unidecode
first_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Phan", "Vũ", "Đặng", "Bùi", "Đỗ"]
last_names = ["An", "Bình", "Châu", "Dũng", "Giang", "Hà", "Hải", "Hùng", "Khánh", "Linh", "Minh", "Nam", "Phúc", "Quang", "Sơn", "Thảo", "Trang", "Tuấn", "Việt", "Yến"]
schools = [
    "Trường THCS Bảo Ninh", "Trường THCS Bắc Nghĩa", "Trường THCS Hải Thành", "Trường THCS Đồng Hải",
    "Trường THCS Lộc Ninh", "Trường THCS số 1 Bắc Lý", "Trường THCS số 1 Nam Lý", "Trường THCS số 1 Đồng Sơn",
    "Trường THCS số 2 Bắc Lý", "Trường THCS số 2 Nam Lý", "Trường THCS Đức Ninh Đông", "Trường THCS Đồng Phú",
    "Trường THCS Đức Ninh", "Trường TH&THCS Quang Phú", "Trường TH&THCS Thuận Đức", "Trường TH&THCS Phú Hải"
]
genders = ["Nam", "Nữ"]

def hash_pwd(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def fake_students(n=50):
    db = Database()
    for i in range(n):
        fname = f"{random.choice(first_names)} {random.choice(last_names)}" 
        fname = f"{random.choice(first_names)} {random.choice(last_names)}"
        uname_base = unidecode.unidecode(fname).replace(" ", "")
        uname = f"{uname_base}{random.randint(10000, 99999)}"
        pwd = hash_pwd("a")
        birth = f"2009-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
        gender = random.choice(genders)
        school = random.choice(schools)
        math_score = round(random.uniform(2, 10), 2)
        literature_score = round(random.uniform(2, 10), 2)
        english_score = round(random.uniform(2, 10), 2)
        first_choice = random.randint(1, 5)
        second_choice = random.randint(1, 5)
        while second_choice == first_choice:
            second_choice = random.randint(1, 5)
        sql = """
            INSERT INTO student (uname, pwd, fname, birth, gender, school, math_score, literature_score, english_score, first_choice, second_choice)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        db.execute(sql, (uname, pwd, fname, birth, gender, school, math_score, literature_score, english_score, first_choice, second_choice))
    print(f"Đã fake {n} thí sinh.")

if __name__ == "__main__":
    fake_students(50)