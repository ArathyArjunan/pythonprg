# rule:
# 1.starts with albhabets or _
# 2. any number of albhabets,digits,_



from re import *
# rule="[a-zA-Z_][a-zA-Z0-9_]*"
# var_name="num_1one"
#
# matcher=fullmatch(rule,var_name)
# if matcher==None:
#     print("invalid")
# else:
#     print("valid")

# rule:
# starting with an alphabet,digit
# special$_
#lengthlimit1,10

rule="[A-Za-z][a-zA-Z$_0-9]{0,10}"
var_name="javathyy_a"
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")
