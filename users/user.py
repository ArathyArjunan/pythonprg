# users=[
#     {"name":"hari","followers":450,"following":900}
#]
f=open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/users/data.txt","r")
user=[]
for line in f:
    text=line.rstrip("\n")
    name,followers,followings=text.split(",")
    print(name,followers,followings)