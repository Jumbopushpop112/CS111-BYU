class LibraryCard:
    #initilization constructor
    def __init__(self, name):
        self.name = name
        self.checkedBooks = []
    #checkout book title
    def checkout_book(self, title):
        if len(self.checkedBooks) == 3:
            return "Limit Reached."
        self.checkedBooks.append(title)
        return f"{title} has been checked out."
    #checking to see if a book is contained
    def has_book(self, title):
        return title in self.checkedBooks
    #return a book
    def return_book(self, title):
        if not title in self.checkedBooks:
            return f"{title} hasn't been checked out."
        else:
            self.checkedBooks.remove(title)
            return f"{title} has been returned."
    #return a string that is formatted nicely containing books checked out
    def __str__(self):
        bookString = ",".join(self.checkedBooks)
        if len(self.checkedBooks) == 0:
            return f"{self.name} has no books checked out."
        else:
            return f"{self.name} has checked out {bookString}"
    #check if two library books objects are equal
    #if the lengths are not the same, why bother comparing?
    #check each title in the first object and if it is not found in the other, they are not equal
    def __eq__(self, other):
        if not len(self.checkedBooks)  == len(other.checkedBooks):
            return False
        for book in self.checkedBooks:
            if not book in other.checkedBooks:
                return False
        return True
