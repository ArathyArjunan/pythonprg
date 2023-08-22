fread=open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/numbers/data.txt","r")
fwrite=open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/numbers/lyear.txt","w")
for line in fread:
    y=int(line.rstrip("\n") )
    if y % 100 == 0 and y % 400 == 0:
        fwrite.write(str(y) + "\n")
    elif y % 100 != 0 and y % 4 == 0:
        fwrite.write(str(y) + "\n")
print("ok")
fread.close()
fwrite.close()