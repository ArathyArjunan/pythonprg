from re import *
rule="[A-Z]{2}[-][0-9]{2}[-][a-zA-Z]{2}[-][0-9]{4}"
var_name="TN-08-bn-4970"
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")
