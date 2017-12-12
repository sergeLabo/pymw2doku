# README #

# Mediawiki to Dokuwiki #

## Transfert d'une liste de pages du wiki Meiawiki vers le dokuwiki ##

### Ce dépot est privé et réservé aux membres de La Labomedia ###

### Installation ###

#### BeautifulSoup
sudo pip3 install bs4

#### pandoc ####
sudo pip3 install pypandoc

### Utilisation ###

#### Quelles pages à transférer ?  ####
Les pages à transférer sont dans le fichier pages_to_upload.txt
Une ligne par pages.
Seulement le nom de page, exemple

 Kivy Buildozer pour créer une application Android avec un script python

#### Python3 ####
Dans le dossier pymw2doku/pymw2doku

python3 download_batch.py

python3 html_to_mw_batch.py

python3 mw_to_doku_batch.py

### Pour relancer ###
Si ça plante, si vous aimez voir défiler le terminal ...

Supprimer les fichiers à relancer de uploaded_pages.txt


### Merci à La Labomedia ###
