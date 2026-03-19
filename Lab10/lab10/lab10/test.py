class library:
    number_books = 10
    def __init__(self, book, author):
        self.book = book
        self.author = author
    def __str__(self):
        return f"{self.book}, {self.author} {self.number_books}"
lib1 = library("The Way of Kings", "Brandon Sanderson")
lib2 = library("Harry Potter", "JK Rowling")
print(lib1)
print(lib2)