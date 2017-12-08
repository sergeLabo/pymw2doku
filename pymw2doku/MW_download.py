#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import sleep
import urllib.request
from urllib.error import HTTPError,URLError
from urllib.parse import quote


class MWDownload:

    def __init__(self, url):
        self.url = url
        self.page = "\n"

    def download_file(self):
        """Télécharge une page"""

        # Open the url
        try:
            page = urllib.request.urlopen(self.url)
            self.page = page.read()  #.decode("utf-8")
            # Ajout d'un EOF
            #self.page += "\n"

            
        # handle errors
        except HTTPError as e:
                print("HTTP Error:", e.code)
        except URLError as e:
                print("URL Error:", e.reason)

    def write_file(self, file_name):
        """Ecrit la page html dans un fichier.
        file_name avec chemin absolu
        """

        with open(file_name, 'wb') as my_file:
            my_file.write(self.page)

        my_file.close()

    def download_and_write(self, file_name):
        """download_and_write"""

        print("Téléchargement de:", file_name)
        self.download_file()
        self.write_file(file_name)


def test1():
    """Download some page"""
    
    site = "https://wiki.labomedia.org/index.php?title=&action=edit"
    edit = "&action=edit"
    
    with open("./input/quelques_pages.txt") as f:
        temp = f.read().splitlines()
        for line in temp:
            print("\nligne", line)
            
            line = quote(line)
            url = site + line + edit
            print("url",url, "\n" )
            
            mw = MWDownload(url)
            mw.download_and_write("./output/pages/" + line)
        f.close()
        
def test2(): 
    """Marche pas Download some file
    https://wiki.labomedia.org/index.php/Fichier:Bubble1.png
    charge la page de description du fichier
    
    il faut beautifull la page pour trouver le
    line = "images/2/2e/Cheminements.png"
    """

    site = "https://wiki.labomedia.org/index.php/"
    
    # Open our local file
    with open("./input/quelques_fichiers.txt") as f:
        temp = f.read().splitlines()
        for line in temp:
            print("\nligne", line)
            
            line = quote(line)
            url = site + line  #+ edit
            print("url",url, "\n" )
            
            mw = MWDownload(url)
            mw.download_and_write("./output/files/" + line)
        f.close()
         
def test3(): 
    """Download one file with path
    https://wiki.labomedia.org/index.php/images/2/2e/Cheminements.png
    """

    site = "https://wiki.labomedia.org/"
    line = "images/2/2e/Cheminements.png"
    name = "Cheminements.png"
    
    url = site + line
    print("url =", url, "\n" )
            
    mw = MWDownload(url)
    mw.download_and_write("./output/files/" + name)

def test4(): 
    """Download on dokuwiki"""

    site = "http://ressources.labomedia.org/"
    line = "Accueil"
    name = "Accueil"
    
    url = site + line
    print("url =", url, "\n" )
            
    mw = MWDownload(url)
    mw.download_and_write("./output/" + name)

if __name__ == '__main__':
    test4()
