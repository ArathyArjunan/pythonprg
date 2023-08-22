num1=int(input("Enter value of num1:"))
num2=int(input("enter value of num2:"))

try:
    res=num1/num2

    print("result",res)
except Exception as e:
    print("exception occured")
    