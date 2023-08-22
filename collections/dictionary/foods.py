items=[
    {"name":"biriyani","price":130,"category":"nonveg"},
    {"name":"dosa","price":70,"category":"veg"},
    {"name":"vegfriedrice","price":130,"category":"veg"},
    {"name":"noodles","price":130,"category":"nonveg"},
    {"name":"burger","price":130,"category":"nonveg"},
]
# print all item names
# ------using map---------
item_name=list(map(lambda it:it.get("name"),items))
print(item_name)
# -------using list comprehension--------------
item=[i.get("name")for i in items]
print(item)

# print all item price
# --using map----------
it_price=list(map(lambda it:it.get("price"),items))
print(it_price)

# ---using list comprehension----------
it_price=[i.get("price")for i in items]
print(it_price)


# print all veg category items

veg_items=list(filter(lambda it:it.get("category")=='veg',items))
print(veg_items)


veg_items=[i for i in items if i.get("category")=='veg']
print(veg_items)