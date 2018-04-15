# Mediawiki to Dokuwiki #

## Transfert d'une liste de pages du wiki Mediawiki vers le dokuwiki ##

Vérifié avec Guillaume

#### Ce dépot est privé et réservé aux membres de La Labomedia ####

### TODO ###

Remplacer ''%% par <code>
Remplacer %%'' par </code>

Arranger en auto les "égal"

Les commandes avec
wget http ...
git clone http ...
svn co http ...
sont fausses: ''%% et %%'' à supprimer

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

Tous les fichiers dokuwiki dans un seul dossier:

    python3 main.py 1


Un dossier par page:

    python3 main.py


### Un dossier par page ###
Tous est dans le dossier ./pymw2doku/pymw2doku/output/one_dir_per_page

Dans le dokuwiki, créer votre page, coller le code dokuwiki,
puis uploader les fichiers.


### Tous les fichiers dokuwiki dans un seul dossier ###
####Les pages à copier####

dans le site dokuwiki: ???/www/dokuwiki/data/pages

sont dans

./pymw2doku/pymw2doku/output/pages/pages/

####Les fichiers à copier####

dans le site dokuwiki: ???/www/dokuwiki/data/media

sont dans

./pymw2doku/pymw2doku/output/media/

### Pour relancer ###
Si ça plante, si vous aimez voir défiler le terminal ...

Pour  retélécharger, et relancer tout

* Supprimer les fichiers à relancer de
    * uploaded_pages.txt
    * uploaded_files.txt

Chaque script peut-être relancé séparément.

### Relance pour créer un dossier par personne  ###

* Mettre à jour
    * uploaded_pages.txt
    * uploaded_files.txt
    * pages_to_upload.txt

Vider:
    * one_dir_per_page

Ne pas supprimer de dossiers, ils ne sont pas créés automatiquement.

Bon, je ne suis pas Alekseï Stakhanoviste, je ne vais pas pinailler un truc qui ne va servir qu'une fois lors d'un wiki-sprint de 4 heures.

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
