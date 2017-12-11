#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
parcours des dossiers, fichiers
puis extrait le code mw
enregistre le code dans /output/mw_code/nom_de_page/nom_de_page.txt

trouve les fichiers à télécharger
télécharge ces fichiers dans /output/mw_code/nom_de_page/
"""


from urllib.parse import quote
from beautiful_mw import BeautifulMW
from mw_download import MWDownload
from my_tools import MyTools

MASTER_DIR = "./output/mw_pages"


def download_files_list(files_list): 
    """Retourne la liste du html des pages des fichiers"""

    site = "https://wiki.labomedia.org/index.php/"
    
    pages_list = []
    for line in files_list:
        print("\nTéléchargemnt de:", line)
        
        line = quote(line)
        url = site + line

        mwd = MWDownload(url, decoded=0)
        file_page = mwd.download_page()
        pages_list.append(file_page)
        
    return pages_list
 
    
class Extract(MyTools):
    
    def __init__(self):
        super().__init__() 
        # Dict répertoires: liste des fichiers 
        self.all_files = self.get_all_files(MASTER_DIR, ".html")
        self.code = ""
        self.deja_vu = []
        
    def extract_code(self):
        """Récupère le code mediawiki
        et l'enregistre dans *.mediawiki
        """
        
        for directory, page in self.all_files.items():
            # page est une liste
            
            # Get code
            bmw = BeautifulMW(page[0])
            bmw.get_code()
            mw_code = bmw.code
            self.code = mw_code
            
            # Write
            # coupe de .html
            fichier = page[0][:-5] + ".mediawiki"

            self.write_data_in_file(mw_code, fichier)
            print("Extraction de ", fichier)
            
    def get_files(self):
        """Retourne la liste des fichiers à partir de 
        self.code = code mediawiki
        
        [[File:tablo-bios.jpg|300px]]
        [[Image:
        [[Fichier:
        """
        
        lines = self.code.splitlines()
        
        for line in range(len(lines)):
            if line not in self.deja_vu:
                # Recherche  [[File:
                 l = self.code[line]
                 print(type(l))
        
    def get_gallery(self):
        """Retourne la liste des fichiers à partir de 
        self.code = code mediawiki  
        <gallery>
        File:tablo-inside.jpg|le dedans
        File:tablo-motherboard2.jpg|la carte mère retournée
        </gallery>
        """
        pass
            
        
def test2(): 
    mt = MyTools()
    file_name = "./output/mw_pages/Le-tablo/Le-tablo.mediawiki"
    data = mt.read_file(file_name)
    extract = Extract()
    extract.code = data
    extract.get_files()
    
    
def test1():
    files_list = [   "Cheminements.png", 
                    "Chimeres-orchestra-11.jpg",
                    "Choisir%20ses%20couleurs%2002.png"]
    pl = download_files_list(files_list)
    print(pl)
    
def main():

    extract = Extract()
    extract.extract_code()
    print("\nExtraction terminée")
    
        
if __name__ == "__main__":
    #main()
    test2()
