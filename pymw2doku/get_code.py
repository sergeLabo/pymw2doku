#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
télécharge sur mw les pages qui sont dans /input/pages_to_transfer.txt

écrit les noms de pages téléchargées dans /input/transfered_pages.txt

puis extrait le code mw

enregistre le code dans /output/mw_code/nom_de_page/nom_de_page.txt

convertit le code en doku

enregistre le code doku dans /output/mw_code/nom_de_page/nom_de_page_doku.txt

télécharge les fichiers cités dans la page dans /output/mw_code/nom_de_page/

si dokuwiki fonctionnel:
upload la page
upload les fichiers

"""
