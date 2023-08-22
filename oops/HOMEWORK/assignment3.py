# Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.

class Student:
    name:str
    age:int
    mark1:int
    mark2:int
    mark3:int
    grade:int
    def __init__(self,name,age,mark1,mark2,mark3):
        self.name=name
        self.age=age
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3

    def total(self):
        total=self.mark1+self.mark2+self.mark3
        if total>=90:
            self.grade='A'
            print("grade=",self.grade)
        elif total<90 and total>=80:
            self.grade='B'
            print("grade=",self.grade)
        elif total<80 and total>=70:
            self.grade='C'
            print("grade=",self.grade)
        elif total<70 and total>=55:
            self.grade='D'
            print("grade=",self.grade)
        else :
            self.grade='E'
            print("grade=",self.grade)
    def set_student(self):
         print("Name:",self.name)
         print("Age:",self.age)
         print("mark1:",self.mark1)
         print("mark2:",self.mark2)
         print("mark3:",self.mark3)

obj=Student('arathy',20,25,35,45)
obj.set_student()
obj.total()



        