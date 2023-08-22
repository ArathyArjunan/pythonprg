f1=open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/attendance/data.txt","r")
f2=open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/attendance/present.txt","r")
total=set()
present=set()
for line in f1:
   total.add(line.rstrip("\n"))

for line2 in f2:
    present.add(line2.rstrip("\n"))
# absent=total.difference(present)
absent=total-present
print(absent)