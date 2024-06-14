class Persona:

    def __init__(self, first_name:str, last_name:str):

        self.first_name = first_name
        self.last_name = last_name
        if type(first_name) != str:
            self.first_name = None
            return "Il nome inserito non è una stringa"
        if type(last_name) != str:
            self.last_name = None
            return "Il cognome inserito non è una stringa"
        if type(first_name) == str and type(last_name) == str:
            self.age = 0
            return first_name, last_name
        if type(first_name) != str and type(last_name) != str:
            self.age = None
        
    def setName(self, first_name:str):
        
        if type(first_name) == str:
            self.first_name = first_name
            return first_name
        else:
            return "Il nome inserito non è una stringa"
    
    def setLastName(self, last_name:str):

        if type(last_name) == str:
            self.last_name = last_name
            return last_name
        else:
            return "Il nome inserito non è una stringa"
    
    def setAge(self, age:int):

        if type(age) == str:
            self.age = age
            return age
        else:
            return "L'età deve essere un numero intero"
    
    def greet(self):

        return f"Ciao, sono {self.first_name} {self.last_name}! Ho {self.age} anni"



persona = Persona(first_name="Gianni", last_name ="Rossi")
print(persona.setName("Gianni"))
print(persona.setLastName("Rossi"))
print(persona.age(23))
print(persona.greet())





        
