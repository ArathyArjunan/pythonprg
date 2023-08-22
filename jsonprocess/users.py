from json import load
with open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/jsonprocess/data.json","r") as f:
    data=load(f)
    # t=max(data,key=lambda k:k.get("total"))
    # print(t)
    # out=sorted(data,reverse=True,key=lambda s:s.get("total"))
    # print(out)
    bca_students=[d.get("name") for d in data if d.get("course")=="bca" ]
    print(bca_students)