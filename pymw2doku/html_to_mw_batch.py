#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
parcours des dossiers, fichiers
puis extrait le code mw
enregistre le code dans /output/mw_code/nom_de_page/nom_de_page.txt

Galère:
    trouve les fichiers à télécharger
    télécharge ces fichiers dans /output/mw_code/nom_de_page/
"""


import os
import re
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import quote
from beautiful_mw import BeautifulMW
from mw_download import MWDownload
from my_tools import MyTools

MASTER_DIR = "./output/mw_pages"


class HtmlToMw(MyTools):

    def __init__(self):
        super().__init__()

        print("Html To Mw")

        # Dict répertoires: liste des fichiers
        self.all_files = self.get_all_files(MASTER_DIR, ".html")

        # Liste des téléchargés
        self.uploaded_file = get_uploaded_file()

        # Liste des téléchargés dans cette instance
        self.uploaded_list = []

    def is_file_un_uploaded(self, fichier):
        """Retourne True si pas encore téléchargé"""

        if fichier in self.uploaded_file:
            return False
        else:
            return True

    def get_mw_and_files(self):
        """Récupère le code mediawiki
        et l'enregistre dans *.mediawiki
        """

        for directory, page in self.all_files.items():
            # page est une liste
            try:
                fichier = page[0]
            except:
                fichier = None

            if fichier:
                sleep(0.1)
                #print("\n\nTraitement de ", fichier)

                # Get code
                bmw = BeautifulMW(fichier)
                mw_code    = bmw.get_mw_code()
                files_list = bmw.get_files_list(mw_code)

                # Write le mediawiki, [:-5] coupe de .html
                fichier = fichier[:-5] + ".mediawiki"

                # Enregistrement du code mediawiki
                self.write_data_in_file(mw_code, fichier)

                # Téléchargement des pages html des fichiers
                pages_list = download_file_page_list(files_list)

                # Récupération de la liste des fichiers
                files_list_with_path = get_files_list_with_path(pages_list)

                # Téléchargement des fichiers
                for f in files_list_with_path:
                    if f:
                        un_uploaded = self.is_file_un_uploaded(f)
                        if un_uploaded:
                            # directory = /media/data/3D/projets/pymw2doku/pymw2doku/
                            print("Téléchargement de", f)
                            download_files_with_path(f, directory)
                            self.uploaded_list.append(f)

        # Enregistrement par ajout au fichier input/uploaded_files.txt
        save_loaded(self.uploaded_list)
        print("Liste des fichiers téléchargés\n", self.uploaded_list)



def download_file_page_list(files_list):
    """Retourne la liste du html des pages des fichiers"""

    site = "https://wiki.labomedia.org/index.php/"

    pages_list = []
    for line in files_list:
        #print("\nTéléchargemnt de:", line)

        line = quote(line)
        url = site + line

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
    si pas dans uploaded_files.txt
    """

    site = "https://wiki.labomedia.org/"

    # line = "images/2/2e/Cheminements.png"
    line = file_with_path

    # name = "Cheminements.png"
    name = os.path.basename(line)

    url = site + line

    mw = MWDownload(url, decoded=0)
    # "./output/mw_files/"
    print("./output/mw_pages/" + directory + "/" + name)

    # download and write effectif du fichier
    mw.download_and_write("./output/mw_pages/" + directory + "/" + name)

def get_uploaded_file():
    """Retourne data de uploaded_files.txt"""

    # Get uploaded_files.txt
    mt = MyTools()
    files_str = mt.read_file("./input/uploaded_files.txt")
    files_str = files_str.splitlines()

    # Conversion du str en list
    uploaded_files = []
    for line in files_str:
        uploaded_files.append(line)

    return uploaded_files

def save_loaded(uploaded_list):
    """Ajoute la liste de uploaded à input/uploaded_files.txt"""

    # Conversion de uploaded_list en str
    lines = ""
    for u in uploaded_list:
        lines = lines + u + "\n"

    # Save
    with open("./input/uploaded_files.txt", 'a') as fd:
        fd.write(lines)
    fd.close()

    print("Ecriture des fichiers nouveaux dans ./input/uploaded_files.txt")

def main():
    """Batch de toutes les pages html to mediawiki
    récup des fichiers cités
    download des pages de fichiers
    download et save des fichiers
    """

    htm = HtmlToMw()
    htm.get_mw_and_files()


if __name__ == "__main__":
    main()
