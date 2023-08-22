weather=[
    {"tvm":25},
    {"apy":23},
    {"kty":27},
    {"idk":18},
    {"ekm":29},
    {"tsr":28},
    {"tvm":26},
    {"apy":22},
    {"kty":28},
    {"idk":19},
    {"ekm":30},
    {"tsr":22},

]
wc={}
for t in weather:
    for k,v in t.items():
        dname=k
        dtemp=v
        if dname in wc:
            old_temp=wc[dname]
            if dtemp>old_temp:
                wc[dname]=dtemp
        else:
                wc[dname]=dtemp
print(wc)
print(max(wc,key=lambda w:wc.get(w)))



items = [
    {"sugar": 45},
    {"tea_powder": 28},
    {"coffee": 67},
    {"dairymilk": 170},
    {"kitkat": 70},
    {"bourborn": 50},
    {"munch": 30},
    {"milk": 80},
    {"pepsi": 99},

]

offers = [
    {"sugar":10},
    {"coffee":20},
    {"milk":5},
  {"pepsi":10}
]

# print today selling price of all items

wc={}
for f in offers:
    for k,v in f.items():
        for i in items:
            for k1,v1 in i.items():
                if k1 in k:
                    wc[k1]=v1-v
                else:
                    wc[k1]=v1
print(wc)


