#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
parcours tous les fichiers *.mediawiki
convertit en doku
enregistre le code doku dans /output/mw_code/nom_de_page/nom_de_page_doku.dokuwiki
"""


import pypandoc
from my_tools import MyTools


MASTER_DIR = "./output/mw_pages"


class Convert(MyTools):

    def __init__(self, directory, page):
        super().__init__()
        self.page = page
        self.directory = directory

    def convert(self):
        """Convertit en syntax doku"""

        in_file = self.page[0]
        out_file = self.page[0][:-10] + '.dokuwiki'

        pypandoc.convert_file( in_file,
                               'dokuwiki',
                               outputfile=out_file)

    def get_file_to_upload(self):
        """Récupère tous les fichiers qu'il faut télécharger"""

        pass

    def upload_file(self):
        """Télécharge les fichiers de la liste"""

        pass


class ConvertBatch(MyTools):

    def __init__(self):
        super().__init__()
        # Dict répertoires: liste des fichiers
        self.all_files = self.get_all_files(MASTER_DIR, ".mediawiki")

    def convert_all(self):
        for directory, page in self.all_files.items():
            conv = Convert(directory, page)
            conv.convert()

def main():

    convert = ConvertBatch()
    convert.convert_all()
    print("\nExtraction terminée")


if __name__ == "__main__":
    main()
