from dottore import Dottore
from paziente import Paziente

class Fattura:

    def __init__(self, patient:list[Paziente], doctor:Dottore):
        
        self.patient = patient
        self.doctor = doctor
        if doctor.isAValidDoctor():
            self.fatture:int = len(patient)
            self.salary:int = 0
        else:
            self.patient = self.doctor = self.fatture = self.salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
    
    def getSalary(self):
        
        if self.patient is not None and self.doctor is not None:
            self.salary = self.doctor.getParcel() * len(self.patient)
            return self.salary
        else:
            return None
    
    def getFatture(self):

        if self.patient is not None:
            self.fatture = len(self.patient)
            return self.fatture
        else:
            return None
    
    def addPatient(self, newPatient:Paziente):
        if type(newPatient) == Paziente:
            self.patient.append(newPatient)
            self.getSalary()
            self.getFatture()
            print(f"Alla lista del Dottor cognome è stato aggiunto il paziente {newPatient.getidCode}")
    
    def removePatient(self, idCode:str):
        for patient in self.patient:
            if patient.getidCode() == idCode:
                self.patient.remove(patient)
                self.getSalary()
                self.getFatture()
                print(f"Alla lista del Dottor {self.doctor} è stato rimosso il paziente {idCode}")

paziente1 = Paziente("Marco", "Bianchi", 40, "P001")
paziente2 = Paziente("Andrea", "Rossi", 35, "P002")
paziente3 = Paziente("Flavio", "Verdi", 28, "P003")
paziente4 = Paziente("Roberto", "Rossi", 45, "P004")
lista_pazienti = [paziente1, paziente2, paziente3]

    # Crea un oggetto Dottore
dottore1 = Dottore("Giovanni", "Verdi", 79, "Pediatra", 100.0)

    # Crea una fattura
fattura = Fattura(lista_pazienti, dottore1)
print(fattura.getSalary())
print(fattura.getFatture())

paziente_da_rimuovere = "P001"
fattura.removePatient(paziente_da_rimuovere)

