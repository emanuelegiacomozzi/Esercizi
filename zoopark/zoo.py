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
        self.health = health

class Fence:
    def __init__(self,area:float, temperature:float, habitat:str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
    
