data={
    "django":"framework",
    "react":"library",
    "fastapi":"framework",
    "vue":"framework",
    "ajax":"library"
}
# wc={}
# values = data.values()
# for v in values:
#     if v in wc:
#         wc[v] += 1
#     else:
#         wc[v] = 1
# print(wc)
#

# wc = {}
# for k,v in data.items():
#     if v in wc:
#         wc[v].append(k)
#     else:
#         wc[v]=[k]
# print(wc)


# q1
text="AABBCCCDE"
# print most recursive character in given text
text="AABBCCCDE"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(max(wc,key=lambda w:wc.get(w)))
print(min(wc,key=lambda w:wc.get(w)))

# q2
text="goodmorning hello goodevening hello"
# print longest word in given text

# using lambda function