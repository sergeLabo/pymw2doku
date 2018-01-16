#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
lance les 3 scripts l'un après l'autre
"""

import os
import sys

from download_batch import main as download_pages
from html_to_mw_batch import main as html_to_mw_and_download_files
from mw_to_doku_batch import main as mw_to_doku


def main(join):
    """Join regroupe les pages et les fichiers
    dans un seul dossier pages et un seul dossier files
    Sinon un dossier par page dans one_dir_per_page
    """

    download_pages(join)
    html_to_mw_and_download_files(join)
    mw_to_doku(join)

if __name__ == "__main__":
    """L'exécution par défaut lance avec join = 0"""

    try:
        if len(sys.argv) == 2:
            if sys.argv[1] == '1':
                a = 1
        if len(sys.argv) == 1:
            a = 0
    except:
        print("""
Usage:

Tous les fichiers dokuwiki dans un seul dossier
    python3 main.py 1

Un dossier par page:
    python3 main.py
""")
        os._exit(0)

    main(a)
