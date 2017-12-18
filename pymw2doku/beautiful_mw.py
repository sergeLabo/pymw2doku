#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import re

from my_tools import MyTools


class BeautifulMW:
    """Extrait le code mw de la page, et le chemin des fichiers."""

    def __init__(self, file_path_name):
        """Chemin absolu avec nom du fichier."""

        self.file_path_name = file_path_name
        self.tools = MyTools()

        # La page à analyser
        page = self.tools.read_file(self.file_path_name)

        # La soupe
        if page:
            self.soup = BeautifulSoup(page, "lxml")
        else:
            self.soup = ""

    def get_mw_code(self):
        """Retourne le code mesiawiki"""

        # <div class="liste-jours">
        c = self.soup.find_all("textarea")

        if len(c) > 0:
            code = c[0].text
        else:
            code = ""
        self.code = code

        return code

    def get_files_list(self, mw_code):
        """Retourne la liste des fichiers à partir de
        mw_code = code mediawiki
        pas de self.code pour test local

        [[File:tablo-bios.jpg|300px]]
        [[Image:
        [[Fichier:
        <gallery>
        File:tablo-inside.jpg|le dedans
        """

        # Récup des fichiers dans la page
        # ((?:Fichier|File|Image):[^|\]\n]+)
        # old ((?:Fichier|File|Image):[^|\]\s]+)
        resp = re.findall( r"((?:Fichier|File|Image):[^|\]\n]+)",
                           mw_code,
                           flags=re.M)

        return resp


def test1():
    file_name = "./output/mw_pages/Le-tablo/Le-tablo.html"
    bmw = BeautifulMW(file_name)
    code       = bmw.get_mw_code()
    files_list = bmw.get_files_list(code)

def test2():
    file_name = "./file_test.mediawiki"

    bmw = BeautifulMW(file_name)
    mt = MyTools()
    test = mt.read_file(file_name)
    files_list = bmw.get_files_list(test)

if __name__ == "__main__":
    test2()
