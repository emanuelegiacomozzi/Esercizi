class Libro:

    def __init__(self, titolo:str, autore:str, stato_prestito = "Disponibile"):
        self.titolo = titolo
        self.autore = autore
        self.stato_prestito = stato_prestito
    def __str__(self):
        return f"Libro = {self.titolo}, autore = {self.autore}, stato_libro = {self.stato_prestito}"

class Biblioteca:

    def __init__(self):
        self.catalogo = []
        
    def aggiungi_libro(self, libro:str):
        self.libro = libro
        self.catalogo.append(libro)
        return f"{libro.titolo} aggiunto al catalogo"
    
    def presta_libro(self, titolo:Libro):
        for libro in self.catalogo:
            if libro.titolo == titolo and libro.stato_prestito == "Disponibile":
                libro.stato_prestito = "Prestato"
                return f"{titolo} prestato"
            else:
                return f"{titolo} non disponibile"
    
    def restituisci_libro(self, titolo:Libro):
        for libro in self.catalogo:
            if libro.titolo == titolo and libro.stato_prestito == "Prestato":
                libro.stato_prestito = "Disponibile"
                return f"{titolo} restituito"
            else:
                return f"{titolo} non in prestito"
    
    def mostra_libri(self):
        libri_disponibili = []
        for libro in self.catalogo:
            if libro.stato_prestito == "Disponibile":
                libri_disponibili.append(libro.titolo)
        if libro.titolo in libri_disponibili:
            return "Libri disponibili:\n" + "\n".join(libri_disponibili)
        else:
            return "Nessun libro disponibile"


biblioteca = Biblioteca()

libro1 = Libro("Lord of the rings", "Paolo" )
print(libro1)

libro2 = Libro("Harry Potter", "Paolo")
print(libro2)

libro3 = Libro("Mia", "Pina")
print(libro3)


print(biblioteca.aggiungi_libro(libro1))
print(biblioteca.aggiungi_libro(libro2))
print(biblioteca.aggiungi_libro(libro3))


print(biblioteca.presta_libro("Lord of the rings"))

print(biblioteca.mostra_libri())

print(biblioteca.restituisci_libro("Lord of the rings"))

print(biblioteca.mostra_libri())

print(biblioteca.presta_libro("Harry Potter"))

print(biblioteca.restituisci_libro("Mia"))

print(biblioteca.mostra_libri())
