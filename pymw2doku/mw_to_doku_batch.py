#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
parcours tous les fichiers *.mediawiki
convertit en doku
enregistre le code doku dans /output/mw_code/nom_de_page/nom_de_page_doku.dokuwiki
"""


import re
import pypandoc
from my_tools import MyTools


MASTER_DIR = "./output/mw_pages"


class Convert(MyTools):

    def __init__(self, page_file):
        super().__init__()
        # page_file est une liste avec un nom de chemin/fichier
        self.page_file = page_file

    def convert(self):
        """Convertit en syntax doku"""

        in_file = self.page_file[0]
        out_file = self.page_file[0][:-10] + '.dokuwiki'

        self.improvement_before(in_file)

        # Appel du Panda magique
        pypandoc.convert_file( in_file,
                               'dokuwiki',
                               outputfile=out_file)

        self.improvement_after(out_file)

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

        page = re.sub( r"(?:__NOTOC__|__NOEDITSECTION__)",
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

    def improvement_after(self, out_file):
        """ACOLACOL to {{
        LOCALOCA to }}
        """
        # Lecture du fichier
        page = self.read_file(out_file)

        page = re.sub( "ACOLACOL",
                        "{{", page, flags=re.M)

        page = re.sub( "LOCALOCA",
                        "}}", page, flags=re.M)

        # Overwrite in_file, pypandoc lira le nouveau fichier
        self.write_data_in_file(page, out_file)


class ConvertBatch(MyTools):

    def __init__(self):
        super().__init__()
        # Dict répertoires: liste des fichiers
        self.all_files = self.get_all_files(MASTER_DIR, ".mediawiki")

    def convert_all(self):
        for directory, page_file in self.all_files.items():
            conv = Convert(page_file)
            conv.convert()


def main():

    convert = ConvertBatch()
    convert.convert_all()
    print("\nExtraction terminée")

def test():
    page_file = ["./convert_test.mediawiki"]
    conv = Convert(page_file)
    conv.convert()
    data = conv.read_file("./convert_test.dokuwiki")


if __name__ == "__main__":
    main()
    # #test()
