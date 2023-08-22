def create_person(**kwargs):
    print(kwargs)
    print(kwargs.get("name"))


create_person(name="hari",age=35,n_place="pkd",j_place="ekm")