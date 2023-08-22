age=int(input("Enter age:"))

#raise
if age<18:
    raise Exception("invalid age")
else:
    print("valid")