from re import *
f1=open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/email/data.txt","r")
vemail=set()
rule="[a-zA-z0-9][a-zA-z0-9_#]*[@]gmail[.]com"
for e in f1:
    e=e.rstrip("\n")
    matcher=fullmatch(rule,e)
    if matcher!=None:
        vemail.add(e)
print(vemail)