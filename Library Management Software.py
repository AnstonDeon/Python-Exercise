class library:

  def __init__(self):
    self.no_of_books = 0
    self.books = []

  def addBook(self, book):
    self.books.append(book)
    self.no_of_books = len(self.books)

  def showInfo(self):
    print(f"THE LIBRARY HAS {self.no_of_books} NUMBER OF BOOKS")
    print("THE BOOKS ARE : ")
    for book in self.books:
      print(book)


l1 = library()
l1.addBook("Harry Potter")
l1.addBook("Aladdin")
l1.showInfo()
