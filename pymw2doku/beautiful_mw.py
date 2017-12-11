#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
from my_tools import MyTools


class BeautifulMW:
    """Extrait le code mw de la page.
    """

    def __init__(self, file_path_name):
        """Chemin absolu avec nom du fichier."""

        self.debug = 0
        self.file_path_name = file_path_name
        self.tools = MyTools()

        # Le fichier à analyser
        self.fichier = self.tools.read_file(self.file_path_name)

    def get_code_and_files(self):
        """Retourne le code mediawiki."""

        soup = BeautifulSoup(self.fichier, "lxml")
        self.get_mw_code(soup)
        self.get_files_list(soup)
        
    def get_mw_code(self, soup):
        # <div class="liste-jours">
        c = soup.find_all("textarea")
        if len(c) > 0:
            self.code = c[0].text
        else:
            self.code = ""
            
    def get_files_list(self, soup):
        """Retourne la liste des fichiers à télécharger
        avec leur chemin
        output/mw_pages/Le-tablo
        """
        
        c = soup.find_all()
        
        print(c)
        self.files_list = []


def test():
    # Chemin relatif
    files = ["./output/mw_pages/Constellation"]

    for f in files:
        bmw = BeautifulMW(f)
        bmw.get_code()

        print("Code\n", bmw.code, "\n")


if __name__ == "__main__":
    test()
