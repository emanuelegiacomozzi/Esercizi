class Pagamento:

    def __init__(self):

        self.__importo:float = 0.0

    def setImporto(self, importo:float):

        self.__importo = importo
    
    def getImporto(self):

        return self.__importo
    
    def dettagliPagamento(self):

        return f"Importo del pagamento: €{self.__importo:.2f}"
    

class PagamentoContanti(Pagamento):

    def __init__(self, importo:float):
        super().__init__()
        self.setImporto(importo)
    
    def dettagliPagamento(self):
        return f"Pagamento in contanti di: €{self.__importo:.2f}"

    def inPezziDa(self):

        banconote:list = [500, 200, 100, 50, 20, 10, 5]
        monete:list = [2,1,0.50,0.20,0.10,0.05,0.01]
        importo = self.getImporto()
        for banconota in banconote:
            pezzi_banconota = importo//banconota
            importo = round(importo - pezzi_banconota * banconota, 2)
        
class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, titolare_carta:str, data:str, num_carta:int):
        super().__init__()
        self.titolare_carta = titolare_carta
        self.data = data
        self.num_carta = num_carta

    def dettagliPagamento(self):
        return f"Pagamento di: €{self.importo:.2f} effettuato con la carta di credito\nNome sulla carta: {self.titolare_carta}\nData di scadenza: {self.data}\nNumero della carta: {self.num_carta}"

carta_credito = PagamentoCartaDiCredito("Mario Rossi", "12/24", 1234567890123456)
print(carta_credito.dettagliPagamento())




#Rendering grafico
from abc import ABC, abstractmethod

class Forma(ABC):

    def __init__(self, nome:str) -> None:
        self.nome = nome
    
    @abstractmethod
    def getArea():

        pass

    @abstractmethod
    def render():

        pass

class Quadrato(Forma):

    def __init__(self, lenght :float) -> None:
        super().__init__(nome)
        nome = "Quadrato"
        self.lenght = lenght
    
    def getArea(self):

        area_quadrato = self.lenght*self.lenght
        return f"Area quadrato: {area_quadrato}"
    
    def render(self):

        lenght = self.lenght
        
        

                    

            
            
        
            





pagamento = Pagamento()
pagamento.setImporto(10)
pagamento.getImporto()
print(pagamento.dettagliPagamento())

pagamento1 = PagamentoContanti()
pagamento1.setImporto(65)
print(pagamento1.dettagliPagamento())
print(pagamento1.inPezziDa())


