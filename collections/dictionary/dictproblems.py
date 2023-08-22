# {key:value,key:value,,,,,,,key:value}

emp = {"id":100,"name":"hari","desig":"HR","salary":250000}
print(emp)

#PRINT EMP NAME

print(emp["name"])

#PRINT EMP SALARY

print(emp["salary"])

#ITERATION OF DICTIONARY

for key in emp:
    print(key,":",emp[key])

#ADDING NEW KEY VALUE PAIR

emp["gender"]="male"
print(emp)

#UPDATING A VALUE

emp["salary"]=27000
print(emp["salary"])
print(emp)

#UPDATING EMPLOYEE SALARY WITH +2000

emp["salary"]+=2000
print(emp["salary"])

#CHECK EXISTENCE OF A KEY

print("name" in emp)
if "name" in emp:
    print("present")
else:
    print("not present")