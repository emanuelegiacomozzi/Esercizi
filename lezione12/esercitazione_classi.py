class Libro:

    def __init__(self, titolo:str, autore:str):
        self.titolo = titolo
        self.autore = autore
        self.stato_prestito = 0

class Biblioteca:

    def __init__(self):
        