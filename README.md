# Mediawiki to Dokuwiki #

## Transfert d'une liste de pages du wiki Mediawiki vers le dokuwiki ##

Vérifié avec Guillaume

#### Ce dépot est privé et réservé aux membres de La Labomedia ####

### Bugs connus ###

* La correction des git clone wget etc ... n'est pas parfaite
* Les pages très compliquées de benj sont très mal traduites, mais un wiki de qualité exige une réécriture de ces pages plutôt qu'un transfert.

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

### Un dossier par page ###
Tous est dans le dossier ./pymw2doku/pymw2doku/output/one_dir_per_page

Dans le dokuwiki, créer votre page, coller le code dokuwiki,
puis uploader les fichiers. Vérifier votre page.

### Pour relancer ###

Pour  retélécharger, et relancer tout

* Supprimer les fichiers à relancer de
    * uploaded_pages.txt
    * uploaded_files.txt

Chaque script peut-être relancé séparément.

### Attention  ###

Bon, je ne suis pas Alekseï Stakhanoviste, je ne vais pas pinailler un truc qui ne va servir qu'une fois lors d'un wiki-sprint de 4 heures.

* Ne pas supprimer les dossiers autres que ceux dans one_dir_per_page, ils ne sont pas créés automatiquement.
* Il faut supprimer le dossier






### Défauts ###
####C'était bien jusqu'à ce que je m'occupe des fichiers !####

Pour trouver les fichiers, je reparse la page html pour trouver les pages des fichiers, que je télécharge, parse, puis je télécharge les fichiers proprement dits.
Proprement, c'est vite dit !

#### Il y a 2 utilisations possibles ####
Et mes explications ne sont pas claires du tout !

#### Je me donne une note ####
Je suis de la vieille école, je sacque: 8/20

Mais je ferais mieux la prochaine fois.

### Merci à La Labomedia ###
