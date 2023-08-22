from re import *
text="aabbcc$#ABC123"
rule="[a-zA-Z0-9]"
matcher=finditer(rule,text)
for m in matcher:
    print(m.group())

# matcher1=finditer("[^a-zA-Z0-9]",text)
# for m in matcher1:
#     print(m.group())

# matcher=finditer("[a-z]",text)
# for m in matcher:
#     print(m.group())

# matcher=finditer("[\w]",text)
# for m in matcher:
#     print(m.group())


matcher=finditer("[\w]",text)
for m in matcher:
    print(m.group())