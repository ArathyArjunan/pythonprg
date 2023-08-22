class Student:
    rolno:int
    name:str
    course:str
    def __init__(self,**kwargs):# **kwargs takes values as dictionary
        self.rolno=kwargs.get("rolno")
        self.name=kwargs.get("name")
        self.course=kwargs.get("course")

    def get_student(self):
        print(self.rolno,self.name,self.course)




obj=Student(rolno=100,name="Arathy",course="django")
obj.get_student()
