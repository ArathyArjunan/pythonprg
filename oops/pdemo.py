class Parent:
    def vehicles(self):
        self.context=["passionpro","swift"]
        return  self.context
class Child(Parent):
    def vehicles(self):
        self.context=super().vehicles()
        self.context.append("hunter")
        return self.context
c=Child()
print(c.vehicles())