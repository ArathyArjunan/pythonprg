word = input("enter a string")
inpt= input("enter a string")
i=word.lower()
j=inpt.lower()
w=sorted(i)
ins=sorted(j)
if w==ins:
    print("words are anagram")
else:
    print("words are not anagram")