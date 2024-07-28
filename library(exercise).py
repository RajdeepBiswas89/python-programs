#write a library class with no_of_books  and books as two instance variables.write a program to create a library from this library class and show how you can print all books,add a book and get the number of books using different methods.show that your program doesnt persist the books after the program is stopped
class library:
    def __init__(self):
        self.numberofbooks=0
        self.books=[]
    def addbooks(self,books):
        self.books.append(books)
        self.numberofbooks=len(self.books)
    def showbooks(self):
        print(f"the library has {self.numberofbooks}")
book1=library()
book1.addbooks("verity")
book1.addbooks("angels and demons")
book1.showbooks()
