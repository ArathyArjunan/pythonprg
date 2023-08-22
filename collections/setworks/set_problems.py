# 1.to remove duplicate from a given list
# lst=[10,20,10,20,12,13,14]
# print(lst)
# s=set(lst)
# print(s)
# lst=list(s)
# print(lst)

# ----suggestions for dq--------
allusers=["mohanlal","fahad","dq","vijay","nivin","asif"]
dq_friendlist=["mohanlal","fahad","asif"]
asif_friendlist=["mohanlal","fahad","vijay","nivin"]
s1=set(allusers)
s2=set(dq_friendlist)
# suggesion=s1.difference(s2)
# suggesion.remove('dq')
# print(suggesion)
# dq-search--> asif mutual friends?
s3=set(asif_friendlist)
mutual=s2.intersection(s3)
print(mutual)

word="pneumonoultramicroscopicssilicovolcanoconiosis"
list=['a','e','i','o','u']
V_count=0
C_count=0
for ch in word:
    if ch in list:
        V_count+=1
        # print(ch)
    else:
        C_count+=1
print("VOWEL COUNT:",V_count)
print("CONSONANT COUNT:",C_count)

