
from re import *
violations=["kl-08-av-2794",
            "kl-08-av-4970",
            "kl-01-av-14",
            "kl-01-av-1",
            "kl-01-av-12",
            "TN-01-av-1",
            "ghz-01-avO-1",
            "kl0-01-av-10"

]

rule="[k][l][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
for v in violations:
    matcher=fullmatch(rule,v)
    if matcher!=None:
        # print(v,"is valid")
     print(matcher.group())
    # else:
    #     print(v,"invalid")
