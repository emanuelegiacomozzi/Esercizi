class Zoo:

    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

    def zookeepers(self, keeper:str):
        self.zoo_keepers.append(keeper)
    
    def _fences(self, fence):
        self.fences.append(fence)
        
    
    def describe_zoo(self):
        for keepers in self.zoo_keepers:
            print("\nGuardians:")
            print(keepers)
            for fence in self.fences:
                if fence in keepers.fences:
                    print("\nFences:")
                    print(fence)
                    print("with animal:")
                    for animal in fence.animals:
                        print(animal)
                    print("\n##############################")
            


class Fence:
    
    def __init__(self, area:float, temperature:int, habitat:str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
    
    def _animals(self,animal:str):
        self.animals.append(animal)

    def __str__(self):
        print()
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"
    
class Animal:

    def __init__(self, name:str, species:str, age:int, height:int, width:int, preferred_habitat:str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age),3)

    def __str__(self):
        print()
        return f"Animal(name={self.name}, species={self.species}, age={self.age}, height={self.height}, width={self.width}, preferred_habitat={self.preferred_habitat})"

    
class ZooKeeper:
        
    def __init__(self,  name:str, surname:str, id:int):
        self.name = name
        self.surname = surname
        self.id = id
        self.fences = []
    
    def __str__(self):
        print()
        return f"Zookeeper(name={self.name}, surname={self.surname}, id={self.id})" 
    
    def add_fences(self, fence):
        self.fences.append(fence)

    
    def add_animals(self,animal:Animal,fence:Fence):
        self.animal = animal
        self.fence = fence
        if fence.area >= animal.height * animal.width and animal.preferred_habitat == fence.habitat:
            fence.animals.append(animal)
            fence.area -= animal.height * animal.width 
            print(f"{animal.name} added to the {fence.habitat} fence")
        else:
            print(f"{animal.name} cannot stay in the {fence.habitat} fence")

    def remove_animal(self, animal:Animal, fence:Fence):
        self.animal = animal
        self.fence = fence 
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += animal.height * animal.width
            print(f"{animal.name} removed from the {fence.habitat} fence.")
    
    def feed_animal(self,animal:Animal):
        self.animal = animal
        for fence in self.fences:
            if animal in fence.animals:
                if fence.area >= animal.height * animal.width:
                    animal.health *= (1 + 1/100)
                    animal.height *= (1 + 2/100)
                    animal.width *= (1 + 2/100)
                    print(f"{animal.name} fed. Health = {animal.health}. Height = {animal.height}. Width = {animal.width}")
                    fence.area -= animal.height * animal.width 
                else:
                    print(f"No space to feed {animal.name} in the {fence.habitat} fence")
    
    def clean(self,fence:Fence):
        self.fence = fence
        if fence.area == 0:
            print("The fence is clean.")
            return fence.area
        cleaning_time:float = fence.area / (sum(animal.height * animal.width for animal in fence.animals))
        fence.area = 0
        print(f"{self.name} {self.surname} cleaned the {fence.habitat} fence. Cleaning time: {cleaning_time}")
        return cleaning_time
    
    def describe_zoo(self,zoo:Zoo):
        zoo.describe_zoo()
            
            
zoo = Zoo()

keeper1 = ZooKeeper("Lorenzo", "Maggi", 1234)
keeper2 = ZooKeeper("Gianni", "Rossi", 1324)
fence1 = Fence(200, 20, "Tropical")
fence2 = Fence(400, 2, "Polar")
animal1 = Animal("Bird", "Canarino", 4, 0.15, 1, "Tropical")
animal2 = Animal("Wolf", "Grey", 23, 1.30, 120, "Tropical")
animal3 = Animal("Bear", "Grizzly", 7, 1.90, 200, "Polar")
fence1._animals(animal1)
keeper2.add_animals(animal3,fence2)
keeper1.add_animals(animal2, fence1)
keeper1.add_fences(fence1)
keeper2.add_fences(fence2)

keeper1.feed_animal(animal1)






zoo.zookeepers(keeper1)
zoo.zookeepers(keeper2)
zoo._fences(fence1)
zoo._fences(fence2)

keeper1.describe_zoo(zoo)










 


    
