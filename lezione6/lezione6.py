class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
emanuele = Person("Emanuele", 20)
print(f"Nome = {emanuele.name}, età = {emanuele.age}")
emanuele.age = 21
print(f"Nome = {emanuele.name}, età = {emanuele.age}")
persona = [Person("Emanuele", 21), Person("Carlo", 22)]
avg_age:float = 0
for person in persona:
    avg_age += person.age
avg_age /= len(persona)
print(f"La media delle età è: {avg_age}")

#esercizio 1
class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
print(bob.age)
if alice.age > bob.age:
    print("Alice is the oldest")
else:
    print("Bob is the best")
emanuele = Person("Emanuele G.", 20)
francesco = Person("Francesco C.", 19)
tiziano = Person("Tiziano R.", 20)
people:list = [alice, bob, emanuele, francesco, tiziano]

min_age:float = float("inf")
index_min_age:int = 0
for i, person in enumerate(people):
    if person.age < min_age:
        min_age = person.age
        index_min_age = 1
person = people[index_min_age]
print(f"Il più giovane è: {person}")

#esercizio 2
class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        self.hobbies:set[str] = set()
    
    def add_hobbies(self, hobbies:list[str]):
        self.hobbies.update(hobbies)
    
    def add_hobby(self, hobby:str):
        self.hobbies.append(hobby)
    
    def remove_hobby(self,hobby):
        if hobby in self.hobbies:
            self.hobbies.remove(hobby)

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, hobbies={self.hobbies})"

alice = Person("Alice", 47)
bob = Person("Bob", 37)
print(alice)
alice.add_hobbies("Calcio", "Cricket")
print(alice)
alice.add_hobbies("Rugby")
print(alice)
alice.remove_hobby("Rugby")
print(alice)