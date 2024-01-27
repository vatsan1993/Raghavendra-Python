import datetime


class Book:
    def __init__(self, id, name, author ):
        self._id = id
        self._name = name
        self._author = author
    def get_id(self):
        return self._id



    def get_name(self):
        return self._name

    def get_author(self):
        return self._author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self._name == other.get_name()
        return False

    def __hash__(self):
        # as we override the equal method and we use the book objects as keys in the dictionary later,
        # we need to override the hash dunder method.
        # the hash dunder method needs to return a hash of unique value.
        return hash(self._id)

    def __str__(self):
        return f'Book id:{self._id} Book Name:{self._name} Author: {self._author}'

    def __repr__(self):
        return f'Book id:{self._id} Book Name:{self._name} Author: {self._author}'

class Library:
    def __init__(self):
        self._books = {}

    def add_book(self, book):
        self._books[book.get_id()] = book

    def get_book_by_id(self, id):
        return self._books.get(id)

    def get_book_by_name(self, book_name):
        for book_id, book in self._books.items():
            if book.get_name() == book_name:
                return book
        return None

    def lend_book(self, book_name):
        book = self.get_book_by_name(book_name)
        if book == None:
            return None
        else:
            self._books.pop(book.get_id())
            return book

    def get_books_by_author(self , author_name):
        books_matching = []
        for book in self._books:
            if book.get_author() == author_name:
                books_matching.append(book)
        return books_matching

    def __str__(self):
        result = []
        for book in self._books:
            result.append(book.get_name())
        return str(result)

class Student:
    def __init__(self, id, name, grade_studying_in):
        self._id = id
        self._name = name
        self._grade_studying_in = grade_studying_in
        self._borrowed_books = {}
        self._total_fine = 0

    def borrow_book(self, book, start_date):
        self._borrowed_books[book] = start_date

    def get_book(self, keyword):
        for book in self._borrowed_books:
            if book.get_id().lower() == keyword.lower():
                return book
            if book.get_name().lower() == keyword.lower():
                return book
        return None

    def return_book(self, search_keyword, end_date):
        book = self.get_book(search_keyword)
        if book == None:
            return None
        else:
            start_date = self._borrowed_books[book]
            self._borrowed_books.pop(book)
            time_delta = end_date - start_date
            days = time_delta.days
            if days < 7:
                self._total_fine += 0
            elif days >= 7 and days < 15:
                self._total_fine += 5
            elif  days >= 15 and days < 21:
                self._total_fine += 7
            elif days > 21 and days < 30:
                self._total_fine += 12
            else:
                self._total_fine += 20
            return book

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def grade_studying_in(self):
        return self._grade_studying_in

    def get_borrowed_books(self):
        return self._borrowed_books.copy()

    def get_total_fine(self):
        return self._total_fine

    def get_num_book_borrowed(self):
        return len(self._borrowed_books)

    def __str__(self):
        result = f'\nStudent id:{self._id} , Student Name: {self._name}, Student Class: {self._grade_studying_in}\n\t'
        book_details = list(map( lambda book: f'Book id:{book.get_id()}, Book name: {book.get_name()}', list(self._borrowed_books.keys())))
        result += '\n\t'.join(book_details)
        return result


class LibraryManagementSystem:
    def __init__(self):
        self._students = []
        self._books = {}

    def add_student(self , student):
        self._students.append(student)
    def add_new_book(self, book):
        self._books[book] = 10
    def get_book(self, book_id):
        for book in self._books:
            if book.get_id() == book_id:
                return book
        return None
    def get_student(self, student_id):
        for student in self._students:
            if student.get_id() == student_id:
                return student
        return None

    def borrow_book(self, book_id, student_id, start_date):
        student = self.get_student(student_id)
        book = self.get_book(book_id)
        if student != None and book != None:
            if self._books[book] != 0:
                student.borrow_book(book, start_date)
                self._books[book] -= 1  # reducing the book count

    def return_book(self, student_id, keyword, end_date):
        student = self.get_student(student_id)
        if student != None:
            book = student.return_book(keyword, end_date)
            if book != None:
                self._books[book] += 1

    def get_fine(self):
        total_fine_collected = 0
        for student in self._students:
            total_fine_collected += student.get_total_fine()
        return total_fine_collected

    def get_student(self, student_id):
        for student in self._students:
            if student.get_id() == student_id:
                return student


    def get_students(self):
        return self._students

    def get_books(self):
        return self._books

def main():
    lib_manage = LibraryManagementSystem()
    books_file_name = "books_ex7.csv"
    students_file_name = "students_ex7.csv"
    with open(books_file_name, 'r')  as books_file:
        data = books_file.readlines()
    for line in data:
        line = line.strip()
        row = line.split(", ")
        id = row[0]
        name = row[1]
        author = row[2]

        book = Book(id, name, author)
        lib_manage.add_new_book(book)

    with open(students_file_name, 'r') as students_file:
        data = students_file.readlines()
    for line in data:
        line = line.strip()
        row = line.split(", ")
        id = row[0]
        name = row[1]
        grade_studying_in = row[2]

        student = Student(id, name, grade_studying_in)
        lib_manage.add_student(student)

    searched_student = lib_manage.get_student("2")
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 2, 1)
    lib_manage.borrow_book("1", "2", start_date)
    lib_manage.borrow_book("2", "2", start_date)
    lib_manage.borrow_book("3", "2", start_date)

    lib_manage.return_book("2", "365 Bedtime Stories", end_date )
    lib_manage.return_book("2", "2", end_date)

    print(searched_student)
    print('fine collected: ', lib_manage.get_fine())

if __name__ == '__main__':
    main()