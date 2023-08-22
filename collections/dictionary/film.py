movies=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":5,"year":2018,"genres":["action","romance","thriller"]}

]
# print all movie names
# for m in movies:
#     print(m.get["name"])


# ----------LIST COMPREHENSION----------------
# movie_name=[m.get("name")for m in movies]
# print(movie_name)
# ----------print filter movie with genre= mystery------------------

# for m in movies:
#     if "mystery" in m.get("genres"):
#         print(m.get("name"))
# --------list comprehension---------------------
# mystery_movie=[m.get("name")for m in movies if "mystery" in m.get("genres")]
# print(mystery_movie)


# ---------top rated movies-----------
# print(max(movies,key=lambda m:m.get("rating")))

# movie name released in 2023

for m in movies:
    if m.get("year")==2023:
        print(m.get("name"))

# ----LIST COMPREHENSION---------

year=[m.get("name")for m in movies if m.get('year')==2023]
print(year)

# sort the movies on the descending order of rating

movie_sort=sorted(movies,reverse=True,key=lambda m:m.get("rating"))
print(movie_sort)

m_movies=[m.get("name")for m in movies if m.get("language")=='malayalam']
print(m_movies)
