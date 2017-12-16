#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Merci à SG1, Stargate:
anneaux_de_transport = voyage facile !

télécharge sur mw les pages qui sont dans /input/pages_to_transfer.txt
mais pas encore transférées

écrit les noms de pages téléchargées dans /input/uploaded_pages.txt

"""

from time import sleep
from urllib.parse import quote
from mw_download import MWDownload
from my_tools import MyTools


# pages à transférées
PAGES_TO_TRANSFERT = "input/pages_to_upload.txt"

# pages transférées
TRANSFERED = "input/uploaded_pages.txt"

SITE = "https://wiki.labomedia.org/index.php?title="
EDIT = "&action=edit"


class UploadManagement(MyTools):
    """Gestion des uploaded."""

    def __init__(self):
        super().__init__()
        self.uploaded = []
        self.unuploaded = []

    def get_uploaded(self):
        """uploaded.txt = str de tous les analysés."""

        transf = self.read_file(TRANSFERED)
        self.uploaded = transf.splitlines()

    def get_unuploaded(self):
        """Retourne les pages non transférées."""

        toutes = self.read_file(PAGES_TO_TRANSFERT)
        toutes_list = toutes.splitlines()

        # Maj de self.uploaded
        self.get_uploaded()

        # All items from tous_list that are not in vu_list
        self.unuploaded = [item for item in toutes_list if item not in self.uploaded]

    def record_uploaded(self):
        """Ajoute les listes uploaded et unuploaded,
        puis enregistre le str.
        """

        # list de pages
        toutes = self.uploaded + self.unuploaded
        # une ligne par item
        toutes_str = '\n'.join(str(line) for line in toutes)
        self.write_data_in_file(toutes_str, TRANSFERED)


class MwPagesBatch(UploadManagement):
    """Class qui va tout lancer."""

    def __init__(self):
        super().__init__()
        self.get_unuploaded()

    def download_unuploaded(self):

        abs_path = self.get_absolute_path("./output/mw_pages/")

        for line in self.unuploaded:
            if line: # Si pas ligne vide
                sleep(0.1)

                # Suppression du / qui définit un sous dossier
                line = line.replace('/', '_')

                # Adreese valide
                page_q = quote(line)
                url = SITE + page_q + EDIT

                mwd = MWDownload(url)
                page = mwd.download_page()

                directory = abs_path + "/" + line + "/"  #page_q + "/"
                self.create_directory(directory)

                fichier = directory + line + ".html"  #page_q + ".html"

                # Ecriture du html
                self.write_data_in_file(page, fichier)

        self.record_uploaded()


def main():

    mpb = MwPagesBatch()
    mpb.download_unuploaded()
    print("Téléchargement terminé")


if __name__ == "__main__":
    main()
