#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
parcours tous les fichiers *.mediawiki
convertit en doku
enregistre le code doku dans /output/mw_code/nom_de_page/nom_de_page_doku.dokuwiki
"""


import re
from unidecode import unidecode
from time import sleep
import pypandoc
from my_tools import MyTools


class Convert(MyTools):

    def __init__(self, page_file, join):
        super().__init__()
        # page_file est une liste avec un nom de chemin/fichier
        self.page_file = page_file
        self.join = join

    def convert(self):
        """Convertit en syntax doku"""

        in_file = self.page_file

        if not self.join:
            out_file = self.page_file[:-10] + '.dokuwiki'
        else:
            # chemin + nom sans extension
            # ./output/pages/work/Kivy: Canvas
            name = self.page_file[19:-10]
            # minuscule
            name = name.lower()
            # Suppr espace
            name = name.replace(" ", "_")
            # Suppr :
            name = name.replace(":", "")
            # Suppr accent
            name = unidecode(name)

            print(name)

            out_file = './output/pages/pages' + name + '.txt'

        self.improvement_before(in_file)

        # Appel du Panda magique
        try:
            pypandoc.convert_file( in_file,
                                   'dokuwiki',
                                   outputfile=out_file)
        except:
            print("\n\nErreur pypandoc avec le fichier:")
            print(in_file, "\n\n")

        self.improvement_after(in_file, out_file)

    def improvement_before(self, in_file):
        """Modifications spéciale Labomedia"""

        # Lecture du fichier
        page = self.read_file(in_file)

        # Suppression des [[Category:]] [[Catégorie:]]
        page = self.delete_category(page)

        # Suppression des __NOTOC__ __NOEDITSECTION__
        page = self.delete_notoc_noeditsection(page)

        # Conversion de <DynamicPageList>
        #page = self.convert_dynamicpagelist(page)

        # Amélioration des balises video
        page = self.change_video_balise(page)

        # Overwrite in_file, pypandoc lira le nouveau fichier
        self.write_data_in_file(page, in_file)

    def add_page_name(self, page, in_file):
        """Ajout en haut de page de
        ===== nom de page =====
        """

        str_list = in_file.rsplit("/")
        name = str_list[-1][:-10]
        name = "=====" + name + "====="

        page = name + "\n" + page

        return page

    def delete_category(self, page):
        """Retourne la page sans [[Category:...]] [[Catégorie:...]]"""

        page = re.sub( r"\s*\[\[(?:Category|Catégorie):[^\]]+\]\]\s*",
                        "",
                        page,
                        flags=re.M)
        return page

    def delete_notoc_noeditsection(self, page):
        """Retourne la page sans __NOTOC__ __NOEDITSECTION__"""

        page = re.sub( r"(?:__NOTOC__|__NOEDITSECTION__)",
                        "",
                        page,
                        flags=re.M)

        return page

    def convert_dynamicpagelist(self, page):
        """Retourne la page sans DynamicPageList

        Dans Mediawiki:
        <DynamicPageList>
        category = Kivy
        count = 30
        order = ascending
        ordermethod = sortkey
        </DynamicPageList>

        Dans dokuwiki:
        <html><DynamicPageList></html>
        category = Kivy
        count = 30
        order = ascending
        ordermethod = sortkey
        <html></DynamicPageList></html>

        Avec https://www.dokuwiki.org/plugin:pagelist
        <pagelist&sort&nouser>
          * [[..:blog:|Blog Plugin]]
        </pagelist>

        """

        page = re.sub( r"",
                        "",
                        page,
                        flags=re.M)

        return page

    def change_video_balise(self, page):
        """Change balise video de mediawiki
        :{{#ev:vimeo|33492100}}
        devient

        {{vimeo>37527145}}
        {{youtube>uDpRWMzCEwo}}

        """

        page = re.sub( r":?\{\{#ev:(\w+)\|([\w_-]+)\}\}",
                        "ACOLACOL\\1>\\2LOCALOCA", page, flags=re.M)

        return page

    def improvement_after(self, in_file, out_file):
        """ACOLACOL to {{LOCALOCA to }}"""

        # Lecture du fichier
        page = self.read_file(out_file)

        if page:
            page = re.sub( "ACOLACOL",
                            "{{", page, flags=re.M)

            page = re.sub( "LOCALOCA",
                            "}}", page, flags=re.M)

            # Ajout ===== nom de page =====
            page = self.add_page_name(page, in_file)

            # Conversion des noms de fichiers


            # Overwrite in_file, pypandoc lira le nouveau fichier
            self.write_data_in_file(page, out_file)
        else:
            print("\n\nConversion impossible pour:\n    ",
                   in_file[17:],
                   "\n\n")


class ConvertBatch(MyTools):

    def __init__(self, join):
        super().__init__()

        self.join = join

        if not self.join:
            dire = "./output/one_dir_per_page"
            # Dict avec répertoires: liste des fichiers
            self.all_files = self.get_all_files(dire, ".mediawiki")
        else:
            dire = "./output/pages"
            self.all_files = self.get_all_files(dire, ".mediawiki")

    def convert_all(self):

        for directory in self.all_files.keys():
            for page_file in self.all_files[directory]:
                #print("Conversion de ", page_file)
                conv = Convert(page_file, self.join)
                conv.convert()


def main(join):
    print("\nConversion:")
    convert = ConvertBatch(join)
    convert.convert_all()
    print("\nConversion terminée")

def test():
    page_file = ["./convert_test.mediawiki"]
    conv = Convert(page_file)
    conv.convert()
    data = conv.read_file("./convert_test.dokuwiki")


if __name__ == "__main__":

    join = 1

    main(join)
    # #test()
