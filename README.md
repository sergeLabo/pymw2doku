# Mediawiki to Dokuwiki #

## Transfert d'une liste de pages du wiki Mediawiki vers le dokuwiki ##

Cet outil télécharge les pages existantes sur un Mediawiki, les convertit en dokuwiki,
et télécharge les fichiers.

Il faut ensuite manuellement créer la page sur le dokuwiki,
coller le code du fichier page.dokuwiki dans votre page.

Puis uploader les fichiers.

### Bugs connus ###

* La correction des git clone ... wget ... etc ... n'est pas parfaite
* Les pages très compliquées (avec des modèles ...) sont mal traduites.

### Installation ###

#### Installation de pip3
    sudo apt-get install python3-dev build-essential
    sudo apt-get install python3-pip

#### BeautifulSoup
    sudo pip3 install bs4 lxml

#### pandoc ####
    sudo apt-get install pandoc
    sudo pip3 install pypandoc

#### unidecode ####
    sudo pip3 install unidecode

### Utilisation ###

#### Quelles pages à transférer ?  ####
Les pages à transférer sont dans le fichier pages_to_upload.txt

Une ligne par pages.

Seulement le nom de page, exemple

    Kivy Buildozer pour créer une application Android avec un script python

#### Excécution ####
Dans le dossier pymw2doku/pymw2doku

    python3 main.py

Tous est dans le dossier ./pymw2doku/pymw2doku/output/

Dans le dokuwiki, créer votre page, coller le code dokuwiki,
puis uploader les fichiers. Vérifier votre page.

### Pour relancer ###

Pour  retélécharger, et relancer tout

* Supprimer les pages à relancer de
    * uploaded_pages.txt

Chaque script peut-être relancé séparément.

### Attention  ###

* Ne pas supprimer le dossier input et les fichiers

** pages_to_upload.txt
** uploaded_pages.txt

### Merci à La Labomedia ###
* Merci à Maxime pour ces regex
* Merci aux utilisateurs de cet outils pour leur patience et leur persévérance
