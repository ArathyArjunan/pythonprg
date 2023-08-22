list1=[1,2,4,5]
for i in range(0,len(list1)
               ):
    element1=list1[i]
    element2=list1[i+1]
    if element2-element1!=1:
        print(element1+1 ,"is mising element")
        break
    else:
     print("consecutive elements")


