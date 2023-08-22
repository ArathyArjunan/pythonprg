from re import *
fr = open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/vehicles/data.txt", "r")
kerala = []
tamilnad = []
krule = "[K][L][-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}"
trule = "[T][N][-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}"
for line in fr:
    veh = line.rstrip(" \n ")
    kmatcher = fullmatch(krule, veh)
    tmatcher = fullmatch(trule, veh)
    if kmatcher != None:
        kerala.append(veh)
    elif tmatcher != None:
        tamilnad.append(veh)
print("Kerala vehicles:", kerala)
print("Tamil nadu vehicles:", tamilnad)
fr.close()