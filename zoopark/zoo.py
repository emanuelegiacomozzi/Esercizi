class Zoo:
    def __init__(self,fences:str,zoo_keepers:str):
        self.fences = fences
        self.zoo_keepers = zoo_keepers

class Animal:
    def __init__(self, name:str, species:str, age:int, height:float, width:float, preferred_habitat:str, health:float):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = (100*(1/age),3)
        

class Fence:
    def __init__(self,area:float, temperature:float, habitat:str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
    
    def add_animal(self,animal:Animal):
        if self.area >= animal.height * animal.width:
            self.animals.append(animal)
            self.area -= animal.height * animal.width
        else:
            print("The animal is too much bigger")

    def remove_animal(self,animal:Animal):
        if self.area < animal.height * animal.width:
                self.animals.remove(animal)
                self.area += animal.height * animal.width
        

class ZooKeeper:
    def __init__(self,name:str,surname:str,id:int):
        self.name = name
        self.surname = surname
        self.id = id
    
    def add_animal(self,animal:str,fence:Fence):
        fence.add_animal(animal)
        
    def remove_animal(self,animal:str,fence:Fence):
        fence.remove_animal(animal)

        

animal = Animal("Elephant","Asiatic",32,5.43,6000.543,"Tropical",health = (100*(1/32),3))
fence = Fence(100, 24, "Tropical")
zoo_keeper = ZooKeeper("Matteo", "Giorgi", 1234)

    
