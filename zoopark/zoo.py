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
    
    def __init__(self, area:int, temperature:int, habitat:str):
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

    
class ZooKeeper(Fence):
        
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
    
    def feed_animal(self,fence:Fence):
        for animal in fence.animals:
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
            return fence.area
        else:
            return 

    def describe_zoo(self,zoo:Zoo):
        zoo.describe_zoo()
            
            
zoo = Zoo()

keeper1 = ZooKeeper("Lorenzo", "Maggi", 1234)
fence1 = Fence(200, 20, "Tropical")
animal1 = Animal("Bird", "Canarino", 4, 0.15, 1, "Tropical")
fence1._animals(animal1)
keeper1.add_fences(fence1)
animal2 = Animal("Wolf", "Black", 10, 1.40, 20, "Tropical")
keeper1.add_animals(animal2,fence1)
keeper1.remove_animal(animal1,fence1)

keeper2 = ZooKeeper("Carlo", "Conti", 1235)
fence2 = Fence(600, 1, "Polar")
keeper2.add_fences(fence2)
animal3 = Animal("Horse", "Black", 10, 2.15, 22, "Polar")
keeper2.add_animals(animal3, fence2)
animal4 = Animal("Bear","Grizzly",20, 1.90, 20, "Polar")
keeper2.add_animals(animal4, fence2)
keeper2.feed_animal(fence2)
keeper1.feed_animal(fence1)

zoo.zookeepers(keeper1)
zoo.zookeepers(keeper2)
zoo._fences(fence1)
zoo._fences(fence2)

keeper1.describe_zoo(zoo)
keeper2.describe_zoo(zoo)








 


    
