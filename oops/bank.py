class Bank:
    acno:int
    balance:int
    ac_type:str
    p_name:str
    def create_account(self,acno,bal,actype,name):
        self.acno=acno
        self.balance=bal
        self.ac_type=actype
        self.p_name=name
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("New Balance",self.balance)
    def withdraw(self,amount):
        if self.balance>=amount:
         self.balance = self.balance - amount
        else:
            print("insuffient balance")
        print(" New Balance", self.balance)


b1=Bank()
b1.create_account(1234,1000,"savings","ravi")
b1.deposit(100)
b1.withdraw(250)