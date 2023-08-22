employee={"id":100,"name":"vijay","department":"hr","salary":25000}

# create a function for returning employee name

# def get_name(emp):
#     return emp.get("name")
# print(get_name(employee))
#
# get_name=lambda emp:emp.get("name")
# print(get_name(employee))

# create a lambda function for returning employee salary

get_sal=lambda emp:emp.get("salary")
print(get_sal(employee))


# *args: positional argument takes any number of parameters type tuple

# def addition(*args):
#     return sum(args)
# print(addition(10,20))
# print(addition(10,20,30))
#
# add=lambda *args:sum(args)+
# print(add(10,20))


def maxinum(*args):
    return max(args)
print(maxinum(10,20,40,50))

maxnum=lambda *args:max(*args)
print(maxinum(101,220,49990,500))

#-----MAX-----------

words=["hello","hi","morning","good"]
# def get_len(w):
#     return len(w)
# print(max(words,key=get_len))

# print(max(words,key=lambda w:len(w)))
# ---------------MIN--------------------
# def get_len(w):
#     return len(w)
# print(min(words,key=get_len))

# print(min(words,key=lambda w:len(w)))

# lst=[1,56,78,2]
# print(sorted(lst,reverse=True))
# print(sorted(lst))

# -----------descending order sorting-----------

# def get_len(w):
#     return len(w)

print(sorted(words,key=lambda w:len(w),reverse=True))
