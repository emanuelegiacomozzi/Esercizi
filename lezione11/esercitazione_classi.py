#cinema 1--->N sale 
#sala -----> film
class Film:

    def __init__(self, titolo:str, durata:int):
        self.titolo = titolo
        self.durata = durata
    
    def __str__(self):
        return(f"Titolo: {self.titolo}\nDurata: {self.durata}")

class Sala:
    
    def __init__(self, id:int, film:Film, posti:int, posti_prenotati:int):
        self.id = id
        self.film = film
        self.posti = posti
        self.posti_prenotati = posti_prenotati
    
    def prenota_posti(self, num_posti:int):
        self.num_posti = num_posti
        self.prenotazione = int(input("Numeri di posti da prenotare: "))
        if self.posti_prenotati == self.posti:
            print("Prenotazione rifiutata. Posti occupati")
        else:
            print("Posti disponibili")
        
    def posti_disponibili(self):
        self.posti_rimanenti =  self.posti_prenotati + self.prenotazione
        self.posti -= self.posti_rimanenti
        return self.posti

    
    def __str__(self):
        return f"ID sala: {self.id}\nFilm in programmazzione: {self.film}\nPosti: {self.posti}\nPosti prenotati: {self.posti_prenotati}"

class Cinema:

    def __init__(self, nome:str):
        self.nome = nome
        self.sale = []
    
    def aggiungi_sala(self, sala:Sala):
        self.sala = sala
        self.sale.append(sala)
    
    def prenota_film(self, titolo_film:Film, num_posti:int):
        self.titolo_film = titolo_film
        self.num_posti = num_posti

    def describe_cinema(self):
        for sala in self.sale:
            print("Sale:")
            print(sala)


#esercizio Magazzino

class Prodotto:

    def __init__(self, nome:str, quantità:int):
        self.nome = nome
        self.quantità = quantità

    def __str__(self):
        return f"Prodotto: {self.nome}\nQuantità: {self.quantità}"

class Magazzino:

    def __init__(self):
        self.prodotti = []
    
    def add_prodotto(self, prodotto:Prodotto):
        self.prodotto = prodotto
        self.prodotti.append(prodotto)
    
    def cerca_prodotto(self, nome:str):
        self.nome = nome
        if self.nome == self.prodotto.nome:
            print(f"\n{self.nome} presente in magazzino")
        else:
            print("Prodotto non presente")
    
    def verifica_disponibiltà(self, nome:str)

magazzino = Magazzino()

prodotto1 = Prodotto("Banana", 30)
prodotto2 = Prodotto("Fragola", 40)
print(prodotto1)
print(prodotto2)

magazzino.add_prodotto(prodotto1)
magazzino.add_prodotto(prodotto2)

magazzino.cerca_prodotto("Banana")