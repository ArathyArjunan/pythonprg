word="observe"
inpt="see"
# # w=sorted(word)
# # ins=sorted(inpt)
# for i in word:
#     if i in inpt:
#         print(i,end=' ')
#


wc={}
is_kangaroo=True
for c in word:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1
for t in inpt:
    if t in wc and wc[c]>0:
        wc[t]-=1
    else:
        is_kangaroo=False
        break
print(is_kangaroo)



