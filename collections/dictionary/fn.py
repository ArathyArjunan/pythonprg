# map():used when we need to perform particular function for all variables

lst=[1,2,3,4,5]
# find squares of all number

# def square(num):
#     return num**2
# squares=list(map(square,lst))
# print(squares)

# using lambda function

# squares=list(map(lambda num:num**2,lst))
# print(squares)
# # ---------find cube of all number---------
# cube=list(map(lambda num:num**3,lst))
# print(cube)


# filter():used to retrieve values based on a condition



lst=[1,2,3,4,5]
# program to print odd number

odd=list(filter(lambda num:num%2!=0,lst))
print(odd)

# program to print even numbers

even=list(filter(lambda num:num%2==0,lst))
print(even)

# program to print num >3
num_gt3=list(filter(lambda num:num>3,lst))
print(num_gt3)