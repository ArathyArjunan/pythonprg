class Employee:
    id:int
    name:str
    designation:str
    salary:int

    def __init__(self,id,name,desg,salary):
        self.id=id
        self.name=name
        self.designation=desg
        self.salary=salary
    def get_emp(self):
        print(self.id,self.name,self.designation,self.salary)

emp1=Employee(1,"rahul","Manager",100000)
emp1.get_emp()
emp2=Employee(2,"ravi","hr",1000)
emp2.get_emp()