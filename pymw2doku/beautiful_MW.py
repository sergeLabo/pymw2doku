#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
from mw2docu_tools import MeteoTools


class BeautifulMW:
    """Fouille dans la page pour trouver les
    températures mini, maxi, type de temps
    des 13 jours suivant le jour/heure courant.

    Retourne un dict de meteo_2017_07_29_01_05_09.html
    Utilise BeautifulSoup.
    """

    def __init__(self, file_path_name):
        """Chemin absolu avec nom du fichier."""

        self.debug = 0
        self.file_path_name = file_path_name
        self.tools = MeteoTools()

        # Le fichier à analyser
        self.fichier = self.tools.read_file(self.file_path_name)

    def get_code(self):
        """Retourne la partie de la page html avec toutes les infos."""

        soup = BeautifulSoup(self.fichier, "lxml")

        # <div class="liste-jours">
        self.code = soup.find_all("textarea")
        

def test():
    # Chemin relatif
    files = ["./pages/1 Kivy: Introduction edit"]

    for f in files:
        forecast = BeautifulMW(f)
        forecast.get_code()

        print("Code\n", forecast.code, "\n")


if __name__ == "__main__":
    test()
