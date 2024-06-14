from persona import Persona 

class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, età:int, specialization:str, parcel:float):
        super().__init__(first_name, last_name)

        self.età = età
        self.specialization = specialization
        self.parcel = parcel

        if type(specialization) != str:

            print("La specializzazione inserita non è una stringa!")
        if type(parcel) != str:

            print("La parcella inserita non è un float")
    
    def setSpecialization(self, specialization:str):

        self.specialization = specialization
        if type(specialization) == str:
            self.specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa")