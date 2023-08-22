# DICTIONARY

emp = {"id":100,"name":"Arathy","desig":"HR","salary":25000}
# print(emp)

# print emp name
print(emp["name"] )
# print salary
# print(emp["salary"])

# iterate dictionary
# for key in emp:
#     print(key,emp[key])

# adding new key value pair
# emp["gender"]="female"
# print(emp)
# emp["salary"]=27000
# print(emp["salary"])
#
# emp["salary"]+=2000
# print(emp["salary"])

# student = {"rollno":22,"name":"alshifa","dept":"bca","mark":80}
# print(student)
# if("dept" in student):
#     print(student["dept"])
#
# #PRINT ALL KEY VALUE PAIR
# for key in student:
#     print(key,student[key])
#
# #ADD NEW KEY VALUE PAIR
# student["grade"]="A"
# print(student)
#
# #REDUCE MARK BY 10
# student["mark"]-=10
# print(student)

# text = "ABABC"
# FIND FIRST RECURSIVE CHARACTER
# wc={}
# count = 0
# for ch in text:
#     if ch in wc:
#         print(ch,"is the first recursive character")
#         break
#     else:
#         wc[ch]=1

# FIND COUNT OF EACH CHARACTER
# wc={}
# for ch in text:
#     if ch in wc:
#         wc[ch]+=1
#
#     else:
#         wc[ch] = 1
#
# print(wc)

words = ["hello","hai","hello","hai","good","morning","evening"]
wc = {}
for i in words:
    if i in wc:
       wc[i] += 1
    else:
        wc[i]=1
print(wc)


