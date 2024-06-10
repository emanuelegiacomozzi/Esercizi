#esercizio 1
class Contatore:

    def __init__(self):
        self.conteggio = 0
    
    def setZero(self):
        self.conteggio = 0
    
    def add1(self):
        self.conteggio += 1
    
    def sub1(self):
        self.conteggio -= 1
        if self.conteggio == 0:
            return f"Non è possibile eseguire la sottrazione Conteggio attuale: 0"

    def get(self):
        return self.conteggio

    def mostra(self):
        print(self.get())
    
c = Contatore()  
c.add1() 
c.sub1()
c.mostra()

#esercizio 2

class RecipeManager:

    def __init__(self):
        self.ricetta:dict = {}
    
    def create_recipe(self, name:str, ingredients:list):

        self.name = name
        self.ingredients = ingredients
        if name not in self.ricetta and tuple(ingredients) not in self.ricetta:
            self.ricetta[name] = ingredients
            return self.ricetta
        if name in self.ricetta and tuple(ingredients) in self.ricetta:
            return "La ricetta esiste già"
    
    def add_ingredient(self, recipe_name:str, ingredient:str):

        self.recipe_name = self.name
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
            return self.ricetta
        elif recipe_name not in self.ricetta or ingredient in self.ricetta:
            return "Errore"
    
    def remove_ingredient(self, recipe_name:str, ingredient:str):
        
        self.ingredient = ingredient
        self.recipe_name = self.name
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            return self.ricetta
        elif recipe_name not in self.ricetta or ingredient not in self.ricetta:
            return "Errore"
    
    def update_ingredient(self,recipe_name:str, old_ingredient:str, new_ingredient:str):
        
        self.remove_ingredient(recipe_name, old_ingredient)
        self.add_ingredient(recipe_name, new_ingredient)
        for recipe_name, self.ingredients in self.ricetta.items():
            self.ingredients[-1], self.ingredients[-2] = self.ingredients[-2], self.ingredients[-1]
            return self.ricetta
        if new_ingredient not in self.ricetta or recipe_name not in self.ricetta:
            return "Errore"
            
    def list_recipes(self):
        for key in self.ricetta.keys():
            return [key]
   
    def list_ingredients(self, recipe_name:str):
        self.recipe_name = recipe_name
        for recipe_name,self.ingredients in self.ricetta.items():
            return self.ingredients
    
    def search_recipe_by_ingredient(self, ingredient:str):
        for self.recipe_name, self.ingredients in self.ricetta.items():
            if ingredient in self.ingredients:
                return self.ricetta
            elif ingredient not in self.ingredients:
                return "Errore"
            

     
        


         
        


manager = RecipeManager()
print(manager.create_recipe("Pizza margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.list_recipes())
print(manager.list_ingredients("Pizza Margherita"))
print(manager.search_recipe_by_ingredient("Farina"))


