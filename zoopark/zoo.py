class Zoo:

    def __init__(self,fences=[], zoo_keepers=[]):
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def add_zookeepers(self, keeper:str):
        self.zoo_keepers.append(keeper)
        
    def add_fences(self, fence:str):
        self.fences.append(fence)

    def add_fences_zookeepers(self):
        print("Guardians:")
        for keepers in self.zoo_keepers:
            print(keepers)
        print("\nFences:")
        for fence in self.fences:
            print(fence)

class ZooKeeper:

    def __init__(self, name:str, surname:str, id:str):
        self.name = name
        self.surname = surname
        self.id = id
    
    def __str__(self):
        return f"Zookeeper(name={self.name}, surname={self.surname}, id={self.id})"
    
    def add_animal(self,animal:str,fence:str):
        fence.add_animal(animal)
    
    def remove_animal(self, animal:str,fence:str):
        fence.add_animal(animal)
    
class Fence:
    
    def __init__(self, area:int, temperature:int, habitat:str, animals=[]):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = animals
    
    def __str__(self):
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"
    
    def add_animal(self,animal:str):
        self.animal = animal
        if self.area >= animal.height * animal.width and animal.preferred_habitat == self.habitat:
            self.animals.append(animal)
            self.area -= animal.height * animal.width
            print(f"{animal} added to the fence.")
        print("\n##############################")
    
    def remove_animal(self,animal:str):
        self.animal = animal
        if animal in self.animals:
            self.animals.remove(animal)
            self.area += animal.height * animal.width
            print(f"The {animal} is too big, remove it to the fence")
        print("\n##############################")
        

class Animal:

    def __init__(self, name:str, species:str, age:int, height:int, width:int, preferred_habitat:str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
    
    def __str__(self):
        return f"Animal(name={self.name}, species={self.species}, age={self.age}, height={self.height}, width={self.width}, preferred_habitat={self.preferred_habitat})"

                 
                 
zoo = Zoo(fences=[], zoo_keepers=[])

keeper1:ZooKeeper = ZooKeeper("Lorenzo","Maggi",1234)
zoo.add_zookeepers(keeper1)
keeper2:ZooKeeper = ZooKeeper("Emanuele","Giacomozzi",2345)
zoo.add_zookeepers(keeper2)

fence1:Fence = Fence(80, 23, "Forest")
fence2:Fence = Fence(600, -45, "Artics")
zoo.add_fences(fence1)
zoo.add_fences(fence2)

zoo.add_fences_zookeepers()

animal1:Animal = Animal("Wolf","Black", 23, 1.00, 80, "Forest")
animal2:Animal = Animal("Bear","Polar", 20, 1.40, 300, "Artics")
keeper1.add_animal(animal1,fence1)
keeper2.add_animal(animal2,fence2)






    
