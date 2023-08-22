#list comprehension
lst=[3,4,5,6,7]
odds=[num for num in lst if num%2!=0]
print(odds)

# for n in lst:
#     if n%2!=0:
#         print(n)
# evens=[num for num in lst if num%2==0]
# print(evens)
#
# cubes=[num**3 for num in lst]
# print(cubes)
#
# num_div=[num for num in lst if num%3==0]
# print(num_div)
# num_div1=[num for num in lst if num%5==0]
# print(num_div1)

#-----nested list---------
lst=[
    [1,2],
    [4,50],
    [50,45]
]

#print all numbers
#
# for sublist in lst:
#     for num in sublist:
#         print(num)
# n=[num for sublist in lst for num in sublist]
# print(n)
#
#print all numbers > 5

# for sublist in lst:
#     for num in sublist:
#         if num > 5:
#             print(num)

#list comprehension in nested list
# number=[num for sublist in lst for num in sublist]
# print(number)

# number=[num for sublist in lst for num in sublist if num >5]
# print(number)


mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphnoe14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]
]

#q1>total number of mobiles
# print(len(mobiles))

#Q2>PRINT ALL  MOBILE NAMES
# for i in mobiles:
#     print(i[1])

# mobile_names=[i[1] for i in mobiles]
# print(mobile_names)

# mobile_names=[i[1] for i in mobiles if i[3]=='4g']
# print(mobile_names)

# for i in mobiles:
#     if i[3]=='4g':
#         print(i[1])


#q3>print mobile name price <30000

# for mob in mobiles:
#     if mob[2]<30000:
#         print(mob[1])

# mname=[mob[1]for mob in mobiles if mob[2]<30000]
# print(mname)

#q4>print mobile names avalable in range of 30000 to 50000

# for mob in mobiles:
#     if mob[2] >=30000 and mob[2]<=50000:
#         print(mob[1])

# mnames=[mob[1]for mob in mobiles if mob[2]>=30000 and mob[2]<=50000]
# print(mnames)

# mnames=[mob[1]for mob in mobiles if mob[2] in range(30000,50001)]
# print(mnames)

#q5>print all mobile names available under 25000
# for mob in mobiles:
#     if mob[2]<25000 and mob[3]=='5g:
#         print(mob[1])

# mname=[mob[1]for mob in mobiles if mob[2]<25000 and mob[3]=='5g']
# print(mname)

items=[
    [1,"potatto",45,"veg",10],
    [1,"tomatto",40,"veg",20],
    [1,"onion",35,"veg",0],
    [1,"brinjal",50,"veg",0],
    [1,"fish",145,"nonveg",10],
    [1,"chicken",145,"nonveg",10],
    [1,"egg",6,"nonveg",100]
]

# total number products
# print in stock product names
# print out of stock product names
# print veg category product names
# product available in range of 50-100
# veg products available in range of 40-80

#1.print(len(items))

# for product in items:
#         if product[4]!=0:
#             print(product[1])

# instock=[product[1] for product in items if product[4]!=0]
# print(instock)

# for product in items:
#         if product[4]==0:
#            print(product[1])


# outstock=[product[1] for product in items if product[4]==0]
# print(outstock)

# for product in items:
#     if product[3]=='veg':
#         print(product[1])


# veg=[product[1] for product in items if product[3]=='veg']
# print(veg)

# for product in items:
#     if product[2] in range(50,100):
#         print(product[1])

# range=[product[1]for product in items if product[2]>=50 and product[2]<=100]
# print(range)

# for product in items:
#     if product[3]=='veg' and product[2] in range(40,81):
#         print(product[1])

r=[product[1]for product in items if product[3]=='veg' and product[2]in range(40,81)]
print(r)

