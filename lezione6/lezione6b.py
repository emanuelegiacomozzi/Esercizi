class Student:
    def __init__(self,name:str, studyProgram:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = None
        self.gender = None
    
    def __str__(self):
        return f"Student(name={self.name},studyProgram={self.studyProgram}, age={self.age}, gender={self.gender})"

    def set_age(self, new_age:int):
        self.age = new_age
    
    def set_gender(self, new_gender:str):
        self.gender = new_gender

emanuele = Student("Emanuele", "Python")
alessandro = Student("Alessandro", "Python")
michele = Student("Michele", "Java")
emanuele.set_age(19)
emanuele.set_gender("M")
alessandro.set_age(25)
alessandro.set_gender("M")
michele.set_age(22)
michele.set_gender("M")
print(emanuele)
print(alessandro)
print(michele)

#esercizio 2
class Animal:
    def __init__(self, name:str):
        self.name = name
        self.legs = None
    
    def set_legs(self, new_legs:int):
        self.legs = new_legs
    
    def get_legs(self):
        return self.legs

    def __str__(self):
        return f"Animal(name={self.name}, lengs={self.legs})"

cane = Animal("Cane")
gatto = Animal("Gatto")
cane.set_legs(4)
gatto.set_legs(4)
print(cane)
print(gatto)

#esercizio 3
class Food:
    def __init__(self,name:str,price:float,description:str):
        self.name = name
        self.price = price
        self.description = description
    
    def __str__(self) -> str:
        return f"{self.name.capitalize()}(price={self.price}, description={self.description})"
    

class Menu:
    def __init__(self,foods:list = []):
        self.foods = foods
   
    def add_food(self, food:Food):
        self.foods.append(food)
    
    def remove_food(self, food:Food):
        if food in self.foods:
            self.foods.remove(food)

pizza = Food("Margherita", 7.00 , "Pomodoro e mozzarella")
pasta = Food("Carbonara", 12.50, "Guanciale, uova e pecorino")
dolce = Food("Cornetto", 3.00, "Cornetto alla crema")
menu = Menu()
menu.add_food(pizza)
menu.add_food(pasta)
print(pizza)
print(pasta)
print(dolce)

'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe restaurant() for each instance.
'''
class Restaurant:
    def __init__(self,name:str,cuisine_type:str):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def description_restaurant(self):
        return f"{self.name.capitalize()}, {self.cuisine_type.capitalize()}"
    
    def open_restaurant(self):
        return f"The restaurant {self.name} is open"

restaurant = Restaurant("Da Pippo", "Pizzeria")
restaurant1 = Restaurant("Carbonaro", "Roman cuisine")
restaurant2 = Restaurant("Mario", "Napoletan cuisine")
print(restaurant.description_restaurant())
print(restaurant1.description_restaurant())
print(restaurant2.description_restaurant())
print(restaurant.open_restaurant())

'''
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.
'''
class User:
    def __init__(self, first_name:str, last_name:str, password:str):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    
    def description_user(self):
        return f"First name = {self.first_name.capitalize()}\nLast name = {self.last_name.capitalize()}\nPassword = {self.password.capitalize()}"
    
    def greet_user(self):
        return f"Hello {self.first_name.capitalize()}, welcome on our site"
    
user = User("Marco", "Rossi", "VzXe45%")
user1 = User("Mario", "Verdi", "HGTyu76")
user2 = User("Laura", "Neri", "ERWLAu7")
print(user.description_user())
print(user.greet_user())
print()
print(user1.description_user())
print(user1.greet_user())
print()
print(user2.description_user())
print(user2.greet_user())



