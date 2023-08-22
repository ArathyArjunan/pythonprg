class Users:
    data = [
        {"id": 1, "username": "jhon", "email": "jhon@gmail.com", "password": "password@123"},
        {"id": 2, "username": "hari", "email": "hari@gmail.com", "password": "password@123"},
        {"id": 3, "username": "ravi", "email": "ravi@gmail.com", "password": "password@123"},
        {"id": 4, "username": "vijay", "email": "vijay@gmail.com", "password": "password@123"},
        {"id": 5, "username": "vinu", "email": "vinu@gmail.com", "password": "password@123"},
        {"id": 6, "username": "tom", "email": "tom@gmail.com", "password": "password@123"},
    ]

    def get(self):
        return self.data
    def retrieve(self,id):
        # for u in self.data:
        #     if u.get("id")==id:
        #         return u
     return [u for u in self.data if u.get("id")==id ]
    def post(self,obj):
        self.data.append(obj)
    def destroy(self,id):
        obj=[u for u in self.data if u.get("id")==id][0]
        self.data.remove(obj)
    def put(self,id,value):
        obj=[b for b in self.data if b.get("id")==id][0]
        pos=self.data.index(obj)
        self.data[pos]=value
student_data={"id":7,"username":"ram","email":"ram@gmail.com","password":"password@123"}
obj=Users()
# obj.post(student_data)
# obj.destroy(5)
student_data1={"id":5,"username":"ram1","email":"ram1@gmail.com","password":"password@123"}
obj.put(5,student_data1)
# print(obj.get())
print(obj.retrieve(5))