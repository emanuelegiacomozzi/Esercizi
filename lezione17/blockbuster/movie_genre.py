from blockbuster.film import Film

class Azione(Film):

    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.genere = "Azione"
        self.penale = 3
    
    def getGenere(self):

        return self.genere

    def getPenale(self):

        return self.penale
    
    def calcolaPenaleRitardo(self, giorni:int):

        

