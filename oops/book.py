


class Book:
    data = [
        {"bid": 1, "bname": "The Christmas Pig", "author": "JK Rowling", "price": 100},
        {"bid": 2, "bname": "Alice in Wonderland", "author": "Lewis Carroll", "price": 200},
        {"bid": 3, "bname": "An Autobiography", "author": "Jawaharlal Nehru", "price": 300},
        {"bid": 4, "bname": "Randamoozham", "author": "M. T.Vasudevan Nair", "price": 400},
        {"bid": 5, "bname": "Pathummayude Aadu", "author": "Vaikom Muhammad Basheer", "price": 500},
        {"bid": 6, "bname": "Aatujeevitham", "author": "Benyamin", "price": 600},
    ]

# to list all details
    def get(self):
        return self.data
# to retreive a book details
    def retrieve(self,id):
        for b in self.data:
            if b.get("bid")==id:
                return b
# to create a new book
    def post(self,obj):
        return self.data.append(obj)
# to delete a data
    def destroy(self,id):
       obj=[b for b in self.data if b.get("bid")==id][0]
       self.data.remove(obj)
# to update a value
    def put(self,id,value):
        obj=[b for b in self.data if b.get("bid")==id][0]
        pos=self.data.index(obj)
        self.data[pos]=value
b1=Book()
# print(b1.retrieve(5))
# book1={"bid":7,"bname":"The Alchemist","Author":"APJ Kalam","price":700}
# b1.post(book1)
# print(b1.get())
# b1.destroy(4)
book2={"bid":6,"bname":"The Alchemist","Author":"APJ Abdulkalam","price":700}
b1.put(6,book2)
print(b1.get())