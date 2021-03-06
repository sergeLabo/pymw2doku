#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Parcours des dossiers, fichiers
puis extrait le code mw
enregistre le code dans /output/nom_de_page/nom_de_page.txt

Fichiers:
    trouve les fichiers à télécharger
    télécharge ces fichiers dans /output/nom_de_page/
"""


import os
import re
from unidecode import unidecode
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote

from beautiful_mw import BeautifulMW
from mw_download import MWDownload
from my_tools import MyTools


class HtmlToMw(MyTools):

    def __init__(self):
        super().__init__()

        print("Html To Mw")

        dire = "./output"
        master_dir = self.get_absolute_path_of_directory(dire)


        # Dict avec répertoires: liste des fichiers
        self.all_files = self.get_all_files(dire, ".html")

        # Liste des téléchargés dans cette instance
        self.uploaded_list = []

    def get_mw_and_files(self):
        """Trouve le code mediawiki et l'enregistre dans *.mediawiki,
        trouve les fichiers à télécharger, et les télécharge.
        
        des clés avec un fichier en valeur
        {'Installation de Twisted':
            ['./output/Installation de Twisted/Installation de Twisted.html'],
         'name': [file.html]
        """

        for directory in self.all_files.keys():
            for page in self.all_files[directory]:
                # Get code
                bmw = BeautifulMW(page)
                mw_code    = bmw.get_mw_code()
                files_list = bmw.get_files_list(mw_code)

                # [:-5] coupe de .html
                page = page[:-5] + ".mediawiki"

                # Enregistrement du code mediawiki
                self.write_data_in_file(mw_code, page)

                # Téléchargement des pages html des fichiers
                pages_list = download_file_page_list(files_list)

                # Récupération de la liste des fichiers
                files_list_with_path = get_files_list_with_path(pages_list)

                # Téléchargement des fichiers
                for f in files_list_with_path:
                    if f:
                        download_files_with_path(f, directory)
                        self.uploaded_list.append(f)


def download_file_page_list(files_list):
    """Retourne la liste du html des pages des fichiers"""

    site = "https://wiki.labomedia.org/index.php/"

    pages_list = []
    for line in files_list:
        if line:
            #line = line.replace("=", ":")
            line = quote(line)
            url = site + "file:" + line

            mwd = MWDownload(url, decoded=1)
            file_page = mwd.download_page()
            pages_list.append(file_page)

    return pages_list

def get_files_list_with_path(pages_list):
    """Retourne liste [ "images/9/9a/Tablo-motherboard3.jpg",
                        "images/2/2e/Cheminements.png"]

    pages_list = [  "html de Tablo-motherboard3.jpg,
                    "html de Cheminements.png]

    <div class="fullMedia"><a href="/images/9/9a/Tablo-motherboard3.jpg"
    class="internal" title="Tablo-motherboard3.jpg">
    """

    files_list_with_path = []

    for page in pages_list:
        if page:
            # Analyse du html pour trouver le chemin du fichier
            soup = BeautifulSoup(page, "lxml")

            for b in soup.find_all("div", class_="fullMedia"):
                c = b.find_all('a', class_="internal")
                file_with_path = c[0].get("href")
                files_list_with_path.append(file_with_path)

    return files_list_with_path

def download_files_with_path(file_with_path, directory):
    """Download one file with path
    https://wiki.labomedia.org/index.php/images/2/2e/Cheminements.png
    """

    site = "https://wiki.labomedia.org/"

    # line = "images/2/2e/Cheminements.png"
    line = file_with_path

    # name = "Cheminements.png"
    name = os.path.basename(line)

    # Minuuscule et sans espace
    doku_name = name.replace(' ', '_').lower()

    url = site + line
    mw = MWDownload(url, decoded=0)

    fichier = "./output/" + directory + "/" + name

    # download and write effectif du fichier
    mw.download_and_write(fichier)
    print("Fichier enregistré: ", name)

def main():
    """Batch de toutes les pages html to mediawiki
    récup des fichiers cités
    download des pages de fichiers
    download et save des fichiers
    """

    htm = HtmlToMw()
    htm.get_mw_and_files()
    print("Done.")


if __name__ == "__main__":

    main()
