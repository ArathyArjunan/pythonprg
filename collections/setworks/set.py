# ----------SET-----------------------------
# mutable,unordered,not allow duplicate,set()
# s={} to create empty dictionary
# -----------------------------------------------
st={10,20,30,'hi'}
# print(st)
# for i in st:
#     print(i)

#     ----------------------------SET METHODS-------------------------
# print(dir(list))
# 1.ADD()
# adding an element into a set
# st = {10,20,30,'hi'}
# st.add(100)
# print(st)
# -----------LIST TO SET--------------
#2.SET()
# lst=[1,2,3,'hello']
# st=set(lst)
# print(st)
# --------------union-------------
# st1={10,11,12,13}
# st2={10,12,25,30}
# union_set=st1.union(st2)
# print(union_set)
# ---------------intersecion---------
# st1={10,11,12,13}
# st2={10,12,25,30}
# intersection_set=st1.intersection(st2)
# print(intersection_set)
# -------------Difference--------------
# st1={10,11,12,13}
# st2={10,12,25,30}
# difference_set=st1.difference(st2)
# print(difference_set)
# ------------------------------------
st1={10,20}
st2={40,50}
st1.update(st2)
print(st1)