class Zoo:

    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

    def zookeepers(self, keeper:str):
        self.zoo_keepers.append(keeper)
        
    def _fences(self, fence:str):
        self.fences.append(fence)
    
    def add_fences_zookeepers(self):
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


class Fence:
    
    def __init__(self, area:int, temperature:int, habitat:str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
    
    def _animals(self,animal:str):
        self.animals.append(animal)
        print("\nwith animal:")
        for animal in self.animals:
            print(animal)

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
    
    def add_animals(self,animal:str,fence:str):
        self.animal = animal
        self.fence = fence
        if fence.area >= animal.height * animal.width and animal.preferred_habitat == fence.habitat:
            fence.animals.append(animal)
            fence.area -= animal.height * animal.width 
            print(f"{animal} added to the fence")
        else:
            print(f"{animal} cannot stay in this fence")

    
    def remove_animals(self,animal:str,fence:str):
        self.animal = animal
        self.fence = fence
        fence.animals.remove(animal)
        fence.area += animal.height * animal.width
        print(f"{animal} removed to the fence")


        

    
    
zoo = Zoo()

keeper1 = ZooKeeper("Lorenzo", "Maggi", 1234)
fence1 = Fence(200, 20, "Tropical")
fence1._animals(Animal("Bird", "Canarino", 4, 0.15, 1, "Tropical"))
keeper1.add_fences(fence1)

keeper2 = ZooKeeper("Carlo", "Conti", 1235)
fence2 = Fence(500, 1, "Polar")
keeper2.add_fences(fence2)

zoo.zookeepers(keeper1)
zoo.zookeepers(keeper2)

zoo.add_fences_zookeepers()

keeper1.add_animals(Animal("Wolf", "Black", 10, 1.40, 90, "Tropical"), fence1)
keeper2.add_animals(Animal("Horse", "Black", 10, 2.15, 200, "Polar"), fence2)







    
