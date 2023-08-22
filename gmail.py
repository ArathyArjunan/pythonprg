# verify a gmail

import re
gmail=input("Enter your gmail:")
g=re.search("@gmail.com$",gmail)
if g:
    print("it is a valid email")
else:
    print("it is invalid")