from abc import ABC,abstractmethod

class Employee(ABC):
    name:str
    salary:int
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

    def salary(self):
        self.salary+=25000
        print("manager salary=",self.salary)

class Developer(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

    def salary(self):
        self.salary +=10000
        print("developer salary=",self.salaraty)

man = Manager("hari",25000)
man.salary()

dev= Developer("vijay",30000)
dev.salary()
