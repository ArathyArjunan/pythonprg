class Parent:
    def mobile(self):
        print("REDMI NOTE 9")
    def car(self):
        print("SWIFT")
    def bike(self):
        print("ROYAL ENFIELD")

class Child(Parent):
    pass

obj=Child()
obj.mobile()
obj.car()
obj.bike()