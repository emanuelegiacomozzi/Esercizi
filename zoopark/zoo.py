class Zoo:

    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

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

class Fence:
    
    def __init__(self, area:int, temperature:int, habitat:str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
    
    def __str__(self):
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"



class ZooKeeper:

    def __init__(self, name:str, surname:str, id:str):
        self.name = name
        self.surname = surname
        self.id = id
    
    def __str__(self):
        return f"Zookeeper(name={self.name}, surname={self.surname}, id={self.id})"
    
zoo = Zoo()

keeper1:ZooKeeper = ZooKeeper("Lorenzo","Maggi",1234)
zoo.add_zookeepers(keeper1)
keeper2:ZooKeeper = ZooKeeper("Emanuele","Giacomozzi",2345)
zoo.add_zookeepers(keeper2)

fence1:Fence = Fence(100, 23, "Tropical")
zoo.add_fences(fence1)

zoo.add_fences_zookeepers()
        


        



    
