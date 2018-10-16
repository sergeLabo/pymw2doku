#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import sleep
import urllib.request
from urllib.error import HTTPError,URLError
from urllib.parse import quote, unquote


class MWDownload:

    def __init__(self, url, decoded=1):
        self.url = url
        self.decoded = decoded
        self.page = ""

    def download_page(self):
        """Télécharge une page ou un fichier."""

        self.page = None
        try:
            page = urllib.request.urlopen(self.url)
            page = page.read()
            if self.decoded:
                self.page = page.decode("utf-8")
            else:
                self.page = page
            name = self.get_name(self.url)
            print("Téléchargement de la page ou du fichier", name)
        except HTTPError as e:
                #print("HTTP Error:", e.code)
                self.download_error()
        except URLError as e:
                #print("URL Error:", e.reason)
                self.download_error(self.page)

        return self.page

    def get_name(self, url):
        """Retourne le nom de page ou de fichier pour print."""

        name = url.replace("https://wiki.labomedia.org/index.php?title=",
                           "")
        name = name.replace("&action=edit",
                            "")
        name = unquote(name)

        return name

    def download_error(self):
        """Imprime les erreurs si 404"""

        print("Erreur téléchargement fichier:")
        print("    url:", self.url)

    def write_file(self, file_name):
        """Ecrit la page html dans un fichier.
        file_name avec chemin absolu
        """

        with open(file_name, 'wb') as my_file:
            my_file.write(self.page)

        my_file.close()

    def download_and_write(self, file_name):
        """download_and_write"""

        self.download_page()
        self.write_file(file_name)


def test0():
    """Download some pages"""

    url = "https://wiki.labomedia.org/index.php/Fichier:Tablo-motherboard3.jpg"
    mw = MWDownload(url)
    mw.download_page()
    print(mw.page)

def test1():
    """Download some pages"""

    site = "https://wiki.labomedia.org/index.php?title="
    edit = "&action=edit"

    with open("./input/pages_to_upload.txt") as f:
        temp = f.read().splitlines()
        for line in temp:
            print("\nligne", line)

            line = quote(line)
            url = site + line + edit
            print("url",url, "\n" )

            mw = MWDownload(url, decoded=0)
            mw.download_and_write(line)
        f.close()

def test2():

    site = "https://wiki.labomedia.org/index.php/"

    # Open our local file
    with open("./input/pages_to_upload.txt") as f:
        temp = f.read().splitlines()
        for line in temp:
            print("\nligne", line)

            line = quote(line)
            url = site + line
            print("url",url, "\n" )

            mw = MWDownload(url, decoded=0)
            mw.download_and_write(line)
        f.close()

def test3():
    """Download one file with path
    https://wiki.labomedia.org/index.php/images/2/2e/Cheminements.png
    """

    site = "https://wiki.labomedia.org/"
    line = "images/2/2e/Cheminements.png"
    name = "Cheminements.png"

    url = site + line
    print("url =", url, "\n" )

    mw = MWDownload(url, decoded=0)
    mw.download_and_write("./output/" + name)

def test4():
    """Download on dokuwiki"""

    site = "http://ressources.labomedia.org/"
    line = "Accueil"
    name = "Accueil"

    url = site + line
    print("url =", url, "\n" )

    mw = MWDownload(url, decoded=0)
    mw.download_and_write("./output/" + name)


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
