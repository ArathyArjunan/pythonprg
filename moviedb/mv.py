from json import load
with open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/moviedb/mdb.json","r",encoding="UTF-8") as f:
    data=load(f)
    print(data)
    print(len(data))# total number of movies in json
    # for d in data:
        # print(d.get("title"))# print all movie name
        #   print(d.get("runtime"))
# print(max(data,key=lambda m:int(m.get("runtime"))))# highest runtime movie

# print all genres

for d in data:
    print(d.get("genres"))
#

# print movie name which contain  genres comedy
comedy_genres=[d.get("title") for d in data if "Comedy" in d.get("genres")]
print(comedy_genres)


# print movie name which contain  genres comedy or Fanstasy

# comedy_genres=[d.get("title") for d in data if ["Comedy","Fantasy"]  in d.get("genres")]
# print(comedy_genres)

# yearwise movie count{1988:5,1984:3}
wc={}
for d in data:
    y=d.get("year")
    if y in wc:
        wc[y]+=1

    else:
        wc[y]=1
print(wc)
