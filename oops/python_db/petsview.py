from get_connection import  db_connect

class Petsview:
    def connect(self):
        db=db_connect(password="",database="animal")
        return db
    
    def get(self):
        db=self.connect()
        cursor=db.cursor()
        query="select * from pets"
        cursor.execute(query)
        qs=cursor.fetchall()
        return qs
    
    def retrieve(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"select * from pets where id={id} "

        cursor.execute(query)
        record=cursor.fetchone() 

        return record
    
    def post(self,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()

        query="insert into pets(age,gender,breed,location,price)" "values(%s,%s,%s,%s,%s)"
        data=tuple(v for v in kwargs.values())
        cursor.execute(query,data)
        db.commit()
        return kwargs

    def destroy(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"delete from pets where id={id}"
    
        cursor.execute(query)
        db.commit()
        return "record deleted"

pv=Petsview()
#print(pv.get())
print(pv.retrieve(2))
print(pv.post(age=21,gender="male",breed="breed3",location="kottayam",price=4000))
print(pv.destroy(3))
