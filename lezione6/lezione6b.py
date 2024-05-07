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