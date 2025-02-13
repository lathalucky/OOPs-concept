# 1. Develop a Library Management System using Inheritance
# Create a Library Management System where:
# • LibraryItem (Base class) contains attributes like title, author, and item_id.
# • Book and Magazine classes inherit from LibraryItem.
# • Book should have an additional genre, and Magazine should have issue_number.
# • Implement a method display_info() that is overridden in child classes to display
# respective details.
#  Test Cases:
# • Create at least two books and one magazine and call display_info() on each
# object.


class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Item ID: {self.item_id}"


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        return f"Book - Title: {self.title}, Author: {self.author}, Item ID: {self.item_id}, Genre: {self.genre}"


class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number

    def display_info(self):
        return f"Book - Title: {self.title}, Author: {self.author}, Item ID: {self.item_id}, issue_number: {self.issue_number}"


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "B001", "Fiction")
book2 = Book("A Brief History of Time", "Stephen Hawking", "B002", "Non-Fiction")

magazine1 = Magazine("National Geographic", "Various", "M001", "2023-10")

print(book1.display_info())
print(book2.display_info())
print(magazine1.display_info())


