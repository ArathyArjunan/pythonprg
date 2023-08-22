class Student:
    rollno:int
    name:str
    course:str
    def add_student(self,rol,name,course):
        self.rollno=rol
        self.name=name
        self.course=course
    def get_student(self):
        print(self.rollno,self.name,self.course)

obj1=Student()
obj2=Student()
obj1.add_student(123,"hari","django")
obj1.get_student()
obj2.add_student(124,"ravi","django")
obj2.get_student()
