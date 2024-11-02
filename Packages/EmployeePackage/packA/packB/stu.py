class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.sname = name
        self.grade = grade

    def displayStudent(self):
        print(self.sid, self.sname, self.grade)
