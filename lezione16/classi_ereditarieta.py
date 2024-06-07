
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
