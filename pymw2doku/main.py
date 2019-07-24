#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys

from download_batch import main as download_pages
from html_to_mw_batch import main as html_to_mw_and_download_files
from mw_to_doku_batch import main as mw_to_doku


"""
Excécute tout

En terminal, dans le dossier de ce script, se lance avec

python3 main.py site edit

Pour Labomedia
    site = "https://wiki.labomedia.org/index.php?title="
    edit = "&action=edit"

"""


import sys

def main(site, edit):

    download_pages(site, edit)
    html_to_mw_and_download_files()
    mw_to_doku()

if __name__ == "__main__":

    print("Liste des arguments", sys.argv)

    try:
        site = sys.argv[1]
        edit = sys.argv[2]
        print(site, edit)
        main(site, edit)
    except:
        print("""
        Usage:
        python3 main.py site edit

        Exemple:
        python3 main.py 'https://wiki.labomedia.org/index.php?title=' '&action=edit'
        """)
        sys.exit()
