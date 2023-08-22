f=open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/numbers/data.txt","w")

for num in range(1890,3001):
    f.write(str(num) + "\n")
print("ok")
f.close()

