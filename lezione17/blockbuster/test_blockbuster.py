import unittest

import sys
import os

# Aggiungi il percorso del modulo al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from movie_genre import Azione, Commedia, Drama
from noleggio import Noleggio

class TestFilm(unittest.TestCase):

    def setUp(self):
        self.filmA1 = Azione(1000, "Jumanji"),
        self.filmA2 = Azione(1001, "Avengers"),
        self.filmA3 = Azione(1002, "Matrix"),
        self.filmA4 = Azione(1003, "Fast and Furious"),
        self.filmA5 = Azione(1004, "Terminator"),
        self.filmC1 = Commedia(2001, "Una notte da leoni"),
        self.filmC2 = Commedia(2002, "Un weekend da bamboccioni"),
        self.filmC3 = Commedia(2003, "Così è la vita"),
        self.filmC4 = Commedia(2004, "Tre uomini e una gamba"),
        self.filmD1 = Drama(3001, "La vita è bella")
        self.films = [self.filmA1, self.filmA2, self.filmA3, self.filmA4, self.filmA5, self.filmC1, self.filmC2, self.filmC3, self.filmC4, self.filmD1]
        self.noleggio = Noleggio(self.films)
    
    def test_isAvaible_True(self):

        film_list = self.films
        self.noleggio = Noleggio(film_list)
        self.assertTrue(self.noleggio.isAvaible(self.filmA1))
