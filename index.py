class Book:
    def __init__(self, title, author, publication_year, genre, available=True):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.is_available = available
    
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Genre: {self.genre}"
    
    def check_availability(self):
        return self.is_available
    
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return f"You have borrowed '{self.title}'."
        else:
            return f"'{self.title}' is currently not available."
        
    def return_book(self):
        self.is_available = True
        return f"You have returned '{self.title}'."
    

class EBook(Book):
    def __init__(self, title, author, publication_year, genre, file_size, format, available=True):
        super().__init__(title, author, publication_year, genre, available)
        self.file_size = file_size  # in MB
        self.format = format
    
    def display_info(self):
        return f"{super().display_info()}, File Size: {self.file_size} MB, Format: {self.format}"
    
    def download(self):
        if self.is_available:
            return f"Downloading '{self.title}'..."
        else:
            return f"'{self.title}' is currently not available for download."
        

class PrintedBook(Book):
    def __init__(self, title, author, publication_year, genre, cover_type, weight, available=True):
        super().__init__(title, author, publication_year, genre, available)
        self.cover_type = cover_type
        self.weight = weight  # in grams
    
    def display_info(self):
        return f"{super().display_info()}, Cover Type: {self.cover_type}, Weight: {self.weight} grams"

    def borrow_book(self):
        return f"{super().borrow_book()} Additionally, please handle the book with care as it is a printed copy."
    
    def get_shipping_cost(self):
        if self.weight <= 500:
            return 5.00 
        elif self.weight <= 1000:
            return 10.00
        else:
            return 15.00
        
class AudioBook(Book):
    def __init__(self, title, author, publication_year, genre, duration, narrator, available=True):
        super().__init__(title, author, publication_year, genre, available)
        self.duration = duration  # in minutes
        self.narrator = narrator
    
    def display_info(self):
        return f"{super().display_info()}, Duration: {self.duration} minutes, Narrator: {self.narrator}"
    
    def listen(self):
        if self.is_available:
            return f"Listening to '{self.title}' narrated by {self.narrator}..."
        else:
            return f"'{self.title}' is currently not available for listening."
        

EBook1 = EBook("Animal Farm", "George Orwell", 1945, "Dystopian Fiction", 2.5, "PDF")
print(EBook1.display_info())
print(EBook1.download())

EBook2 = EBook("1984", "George Orwell", 1949, "Dystopian Fiction", 3.0, "EPUB", available=False)
print(EBook2.display_info())
print(EBook2.download())

PrintedBook1 = PrintedBook("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", "Hardcover", 600)
print(PrintedBook1.display_info())
print(PrintedBook1.borrow_book())
print(PrintedBook1.get_shipping_cost())

PrintedBook2 = PrintedBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", "Paperback", 300, available=False)
print(PrintedBook2.display_info())
print(PrintedBook2.borrow_book())
print(PrintedBook2.get_shipping_cost())

AudioBook1 = AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 300, "Rob Inglis")
print(AudioBook1.display_info())
print(AudioBook1.listen())


