#Exercise 1: Creating an Abstract Class with Abstract Methods
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod

    def area():

        pass

    def perimeter():

        pass


class Circle(Shape):

    def __init__(self, radius:float) -> None:
        super().__init__()

        self.radius = radius
        self.area_circle = 3.1415 * radius**2
        self.perimeter_circle = radius * 3.1415**2
    
    def area(self):
        return self.area_circle
    
    def perimeter(self):
        return self.perimeter_circle
    
circle = Circle(radius=12)
print("Circle area: ", circle.area())
print("Circle perimeter: ", circle.perimeter())

class Rectangle(Shape):

    def __init__(self, base:float, half:float) -> None:
        super().__init__()

        self.base = base
        self.half = half
        self.area_rectangle = base * half
        self.perimeter_rectangle = base*2 + half*2
    
    def area(self):
        return self.area_rectangle
    
    def perimeter(self):
        return self.perimeter_rectangle

rectangle = Rectangle(base=11.2, half=5)
print("Rectangle area: ", rectangle.area())
print("Rectangle perimeter: ", rectangle.perimeter())

#Exercise 2: Implementing Static Methods

class MathOperations:

    @staticmethod
    def add(num1,num2):
        return num1+num2
    
    @staticmethod
    def mutiply(num1,num2):
        return num1*num2

print("Num sum: ", MathOperations.add(10,20))
print("Num product: ", MathOperations.add(15,10))

#Exercise 3: Library Management System 

class Book:

    def __init__(self,title:str, author:str, isbn:int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"title = {self.title}, author = {self.author}, isbn = {self.isbn}"
    
    @classmethod
    def from_string(cls, book_str:str):
        title, author, isbn = book_str.split(',')
        return cls(title, author, isbn)

book_str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia = Book.from_string(book_str)

print(divina_commedia)

class Member:

    def __init__(self, name:str, member_id:int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_books(self, book:str):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            return self.borrowed_books 
    
    def return_book(self,book:str):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{book} isn't borrow")
        return self.borrowed_books
    

    def __str__(self) -> str:
        borrowed_title_list = []
        for book in self.borrowed_books:
            borrowed_title_list.append(book.title)
        borrowed_title = ','.join(borrowed_title_list)
        return f"name = {self.name}, member_id = {self.member_id}, borrowed books = {borrowed_title}"

    @classmethod
    def from_string(cls, member_str:str):
        name, member_id = member_str.split(',')
        return cls(name, member_id)

member_str = "Paolo, 12345"
member1 = Member.from_string(member_str)
print(member1)

member1.borrow_books(divina_commedia)
print(member1)

member1.return_book(divina_commedia)
print(member1)

#Exercise 4: University Management System

class Person(ABC):

    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    def get_role():

        pass

    def __str__(self):
        return f"Name={self.name}, age={self.age}"
    
class Student(Person):

    def __init__(self, name: str, age: int, student_id:str) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
    
    def get_role(self):
        return "Student"
    
    def enroll(self, course):
        self.courses.append(course)
        return self.courses
    
studente1 = Student(name="Pippo", age= 18, student_id=1234)
print(studente1)

print(studente1.get_role())

print("Student1 courses:", studente1.enroll("Math"))
print("Student1 course:", studente1.enroll("History"))
