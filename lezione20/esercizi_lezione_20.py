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

    def __init__(self):
        super().__init__()
    
    def dettagliPagamento(self):
        return f"Pagamento in contanti di: €{self.__importo:.2f}"

    def inPezziDa(self):

        importo = self.getImporto()
        banconote:list = [500, 200, 100, 50, 20, 10, 5]
        
        monete:list = [2,1,0.50,0.20,0.10,0.05,0.01]
        for banconota in banconote:
            pezzi_banconota = self.importo//banconota
            if pezzi_banconota > 0:
                self.risultato[]

        
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
                    

            
            
        
            





pagamento = Pagamento()
pagamento.setImporto(10)
pagamento.getImporto()
print(pagamento.dettagliPagamento())

pagamento1 = PagamentoContanti()
pagamento1.setImporto(65)
print(pagamento1.dettagliPagamento())
print(pagamento1.inPezziDa())


