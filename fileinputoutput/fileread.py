
# f1=open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/fileinputoutput/data.txt","r")
# w=[]
# for line in f1:
#     text=line.rstrip("\n").split(" ")
#     for t in text:
#       w.append(t)
# print(w)

f1=open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/fileinputoutput/data.txt","r")
w=set()
for line in f1:
    text=line.rstrip("\n").split(" ")
    for t in text:
      w.add(t)
print(w)