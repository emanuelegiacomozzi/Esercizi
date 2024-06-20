from movie_genre import Azione, Commedia, Drama

class Noleggio:

    def __init__(self, film_list:list[str]):

        self.film_list = film_list
        self.rented_film:dict = {}
    
    def isAvaible(self, film:str):

        titolo_film = film
        if film not in self.film_list:
            print(f"Il film scelto non è disponibile: {titolo_film}! ")
            return False
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {titolo_film}!")
            return True
               