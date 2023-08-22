import mysql.connector
def db_connect(host="localhost",user="root",password=None,database=None):
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database=database
    )
    return db