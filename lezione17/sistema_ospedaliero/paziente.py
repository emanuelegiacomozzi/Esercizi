from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str, age:int, idCode:str):
        super().__init__(first_name, last_name)
    
        self.age = age  
        self.idCode = idCode
    
    def setIdCode(self, idCode:str):

        self.idCode = idCode
    
    def getidCode(self):

        return self.idCode
    
    def patientInfo(self):

        print(f"Paziente: {self.first_name} {self.last_name}\nID: {self.idCode}")

paziente = Paziente("Mattia", "Neri", 34, "Hb34")
paziente.setIdCode("Hnbcd")
print(paziente.getidCode())
paziente.patientInfo()
