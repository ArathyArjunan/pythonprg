from json import load
with open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/restcountries/rest.json",encoding="UTF-8") as f:
    data=load(f)
# print the of countries
print(len(data))

# ----------print all country names----------------------------
# for d in data:
#     print(d.get("name"))
# country_names=[ d.get("name")for d in data]
# print(country_names)
# ----- print all region names--------
# region={d.get("region")for d in data}
# print(region)

# -----------print asian country names------------
# asian_country=[d.get("name")for d in data if "Asia" in d.get("region")]
# print(asian_country)

# print population of afganisthan

# populatipon=[d.get("population")for d in data if d.get("name")=="Afghanistan"]
# print(populatipon)
#
# for d in data:
#     if d.get("name")=="Afghanistan":
#         print(d.get("population"))

# print indian borders
# for d in data:
#     if d.get("name")=="India":
#         print(d.get("borders"))

#
# country_borders=[d.get("borders")for d in data if d.get("name")=="India"][0]
# print(country_borders)
# country_borders_names=[c.get("name")for c in data if c.get("alpha3Code") in country_borders]
# print(country_borders_names)


# indian currency code
# for d in data:
#     if d.get("name")=="India":
#         b=d.get("currencies")
#         for c in b:
#             print(c.get("code"))

currency=[d.get("currencies")for d in data if d.get("name")=="India"][0]
print(currency[0].get("code"))


# country with highest population

print(max(data,key=lambda d:d.get("population")))


