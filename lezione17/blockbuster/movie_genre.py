from blockbuster.film import Film

class Azione(Film):

    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        genere = "Azione"
        penale = 3
