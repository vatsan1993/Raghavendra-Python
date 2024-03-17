class Document:
    def __init__(self, title, num_pages):
        self.__num_pages = num_pages
        self.__title = title

    def get_num_pages(self):
        return self.__num_pages

    def get_title(self):
        return self.__title

    def __str__(self):
        return f'Title: {self.__title}, Pages: {self.__num_pages}'

    def __repr__(self):
        return f'{self.__title}, {self.__num_pages}'


class Certificate(Document):
    def __init__(self, title, num_pages, provided_by, expiration_date):
        super().__init__(title, num_pages)
        self.__provided_by = provided_by
        self.__expiration_date = expiration_date

    def get_provided_by(self):
        return self.__provided_by

    def get_expiration_date(self):
        return self.__expiration_date

    def __str__(self):
        return "Cert{" + super().__str__() + f', Issued By: {self.__provided_by}, Expires on: {self.__expiration_date}' +"}"

    def __repr__(self):
        return "Cert{" + super().__repr__() + f', {self.__provided_by}, {self.__expiration_date}' + "}"


class Email(Document):
    def __init__(self, title, sender, receiver, message):
        super().__init__(title, round(len(message)/1000 + 1))
        self.__sender = sender
        self.__receiver = receiver
        self.__message = message

    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def __str__(self):
        return "Email{" +super().__str__() + f', Sender: {self.__sender} , Receiver: {self.__receiver}' +"}"

    def __repr__(self):
        return "Email{" +super().__repr__() + f', {self.__sender}, {self.__receiver}' + '}'


class Book(Document):
    def __init__(self, title, num_pages, author):
        super().__init__(title, num_pages)
        self.__author = author

    def get_author(self):
        return self.__author

    def __str__(self):
        return "Book{" +super().__str__() + f", Author: {self.__author}" + "}"

    def __repr__(self):
        return "Book{" +super().__repr__() + f', {self.__author}' +"}"



cert1 = Certificate("Python Professional Certification", 1, "Microsoft", "14/08/2029")
cert2 = Certificate("Java Enterprise Certification", 1, "Oracle", "14/08/2029")

email = Email("Bug in App", "abc123@gmail.com", "appcustomercase@gmail.com", "There is a bug in the app.")

book = Book("How to Code", 300, "Max Winchester")

print(cert1)
print(cert2)
print(email)
print(book)

documents = [cert1, cert2, email, book]
print(documents)



print(isinstance(cert1, Certificate))
print(isinstance(email, Email))
print(isinstance(book, Book))

print(isinstance(book, Certificate))
print(isinstance(email, Book))
print(isinstance(cert1, Email))

print(isinstance(cert1, Document))
print(isinstance(email, Document))
print(isinstance(book, Document))


