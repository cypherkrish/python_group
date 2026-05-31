from teacher import Teacher
class Student(Teacher):
    def setmarks(self, marks):
        self.marks = marks
    def getmarks(self):
        return self.marks