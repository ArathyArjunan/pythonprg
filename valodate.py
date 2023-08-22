# import re
# # text="aaaabbbcc"
# # text1="abababab"
# #
# # t=re.search("[a]{4}",text)
# # t1=re.search("[a]{4}",text1)
# #
# # print(t)
# # print(t1)
#
# te="abcbcd"
# check=re.search("[a-z]{4}",te)
# print(check)
#
#
# stri="3457abDARG5678"
# st="abDARG5678"
# s1=re.search("[a-z]{2}[A-Z]{4}",st)
# print(s1)
# s=re.search("[a-z]{2}[A-Z]{4}",stri)
# print(s)
# # mobile number verification
#
from re import *
mobile_no=input("enter a mobile number:")
s = search("^[+91][0-9]{10}",mobile_no)
if s:
    print("valid number")
else:
    print("not a valid number")

