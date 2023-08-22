from abc import ABC,abstractmethod

class Employee(ABC):
    id:int
    name:str
    bpay:int
    hra:int
    pf:int
    salary:int
    def _init_(self,id,name,bpay,hra,pf):
        self.id=id
        self.name=name
        self.bpay=bpay
        self.hra=hra
        self.pf=pf

    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def __init__(self,id,name,bpay,hra,pf):
        super()._init_(id,name,bpay,hra,pf)

    def salary(self):
        self.salary=self.bpay+self.hra-self.pf
        print("manager salary=",self.salary)

class Developer(Employee):
    def __init__(self, id, name, bpay, hra, pf):
        super()._init_(id, name, bpay, hra, pf)

    def salary(self):
        self.salary = self.bpay + self.hra - self.pf
        print("developer salary=",self.salary)

man = Manager(1,"hari",1000,500,100)
man.salary()

dev= Developer(2,"vijay",2000,1000,200)
dev.salary()
