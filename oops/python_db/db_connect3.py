import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="animal"
)
cursor=mydb.cursor()
query="""
insert into pets(age,gender,breed,location,price)values(12,'female','breed2','kozhikode',25000)"""
cursor.execute(query)
mydb.commit() #save changes