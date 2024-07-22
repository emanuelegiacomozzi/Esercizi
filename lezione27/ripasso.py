class RecipeManager:

    def __init__(self):

        self.dizionario:dict = {}
    
    def create_recipe(self, name:str ,ingredients:list):
        self.name = name
        self.ingredients = ingredients
        if name not in self.dizionario:
            self.dizionario[name] = ingredients
            return self.dizionario
        else:
            return "La ricetta esiste"
    

    def add_ingredient(self, recipe_name:str, ingredient:str):
        recipe_name = self.name
        if recipe_name in self.dizionario:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)
                return self.dizionario
            else:
                return "L'ingrediente esiste già"
    
    
    def remove_ingredient(self, recipe_name:str, ingredient:str):
        self.ingredient = ingredient
        if recipe_name in self.dizionario:
            if ingredient in self.ingredients:
                self.ingredients.remove(ingredient)
                return self.ingredients
            else:
                return "L'ingrediente non esiste"
    
    
    def update_ingredient(self, recipe_name:str, old_ingredient:str, new_ingredient:str):
        if recipe_name in self.dizionario:
            self.remove_ingredient(recipe_name, old_ingredient)
            self.add_ingredient(recipe_name, new_ingredient)
            self.ingredients[-1], self.ingredients[-2] = self.ingredients[-2], self.ingredients[-1]
            return self.dizionario
        else:
            return "L'ingrediente non esiste"
    
    def list_recipes(self):
        for self.recipe_name, self.ingredients in self.dizionario.items():
            return f"{self.recipe_name}, {self.ingredients}"
    

    def list_ingredients(self, recipe_name:str):
        if recipe_name in self.dizionario:
            return self.ingredients
    

    def search_recipe_by_ingredient(self, ingredient:str):
        if self.recipe_name in self.dizionario:
            if ingredient in self.ingredients:
                return [self.recipe_name]
            else:
                return "Nessuna ricetta contiene l'ingrediente"            

    

    

    

    

manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.list_ingredients("Pizza Margherita"))
print(manager.list_recipes())
print(manager.search_recipe_by_ingredient("Basilico"))