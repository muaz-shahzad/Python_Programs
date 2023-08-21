class Library:
    no_of_books = 0
    list = []

    def __init__(self):
        self.name = None

    def add(self,name):
        self.list.append(name)
        self.no_of_books += 1

    def showBook(self):
        if len(self.list) == self.no_of_books:
            print(f"Books List {self.list}")
            print(f"No oF Books {self.no_of_books}")


obj = Library()
obj.add("Computer Science")
obj.add("Science")
obj.add("PST")
obj.add("Maths")
obj.showBook()


