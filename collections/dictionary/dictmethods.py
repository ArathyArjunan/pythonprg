student={"rollno":100,"name":"Arathy","age":25,"course":"mca"}
# ---------to return values--------
print(student.values())
# ---------to return keys--------
print(student.keys())
# ---------to return both keys and values--------
print(student.items())

for k,v in student.items():
    print(k,v)

# ----to get values from key-----------------
# print(student["name"]) # if we insert an invalid key the entire program execution will  stop
print(student.get("name")) # if we insert an invalid key the entire program execution will not  stop instead it returns none and continues execution


# -----------to remove a key value pair -----------
student.pop("course")
print(student)