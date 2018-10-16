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

    def __init__(self, page_file):
        super().__init__()
        # page_file est une liste avec un nom de chemin/fichier
        self.page_file = page_file

    def convert(self):
        """Convertit en syntax doku"""

        in_file = self.page_file

        out_file = self.page_file[:-10] + '.dokuwiki'

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

        # Titre en H1, 6égal
        name = "======" + name + "======"

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

            # correction des nombres d'égal
            page = self.egal_improvement(page)

            # corrections des adresse http
            # git clone https://git...
            # git clone http://git...
            page = self.correction_address(page)

            # remplacement des ''%%  par espace espace
            # suppression des %%''
            # suppression des %%''\\espace
            page = self.delete_quote_pourcent(page)

            # Correction des fiches idées avec mauvais liens images
            page = self.correction_bad_image(page)

            # Overwrite in_file
            self.write_data_in_file(page, out_file)
        else:
            print("\n\nConversion impossible pour:\n    ",
                   in_file[17:],
                   "\n\n")

    def egal_improvement(self, page):
        """correction des nombres d'égal"""

        lines = self.get_lines_in_page(page)
        # page sans titre
        lines_sans_titre = lines[1:]
        # titre
        titre = lines[0]
        new_page = titre + "\n"

        # y a-t-il des 6 egal dans la page autre que le titre
        egal = False
        for line in lines_sans_titre:
                if "======" in line:
                    egal = True

        if egal:
            print("Correction des égal")
            # parcours de toutes les lignes une seule fois
            for line in lines_sans_titre:
                if "======" in line:
                    line = line.replace("======", "=====")
                elif "=====" in line:
                    line = line.replace("=====", "====")
                elif "====" in line:
                    line = line.replace("====", "===")
                elif "===" in line:
                    line = line.replace("===", "==")
                elif "==" in line:
                    line = line.replace("==", "=")

                # reconstruction de page
                new_page += line + "\n"
        else:
            # parcours de toutes les lignes une seule fois
            for line in lines_sans_titre:
                # reconstruction de page
                new_page += line + "\n"

        return new_page

    def delete_quote_pourcent(self, page):
        """remplacement des ''%%  par espace espace
        suppression des %%''
        suppression des %%''\\espace
        """

        # ''%% en début de ligne
        page = page.replace("''%%", "  ")

        # ''%% en fin de ligne avec \\espace
        # https://regex101.com/r/MMtxW2/1
        page = re.sub( r"(%%''\\\\)",
                       "",
                       page,
                       flags=re.M)

        # en fin de ligne
        page = page.replace("%%''", "")

        return page

    def correction_address(self, page):
        """ git clone https://git...
            git clone http://git...
            wget http://...

''%%wget %%''[[http://oscpack.googlecode.com/files/oscpack.zip|''%%http://oscpack.googlecode.com/files/oscpackzip%%'']]
    espace espace wget http://...files/oscpack.zip
        """

        lines = self.get_lines_in_page(page)
        # page sans titre
        lines_sans_titre = lines[1:]
        new_page = ""

        cmd = ["wget", "git clone", "svn co"]

        for line in lines:
            for c in cmd:
                if c in line:
                    print("Commande à corriger\n    ", line)

                    # coupe de la fin
                    line = line.split("|", 1)[0]

                    # TODO à vérifier sur beaucoup de page
                    line = line.replace("''%%[[", "")
                    line = line.replace("''%%", "")
                    line = line.replace("]]%%''", "")
                    line = line.replace("%%''", "")

                    print("Commande corrigée\n    ", line)

            # reconstruction de page
            new_page += line + "\n"

        return new_page

    def get_lines_in_page(self, page):
        """Retourne les lignes dans une liste"""

        lines = page.splitlines()

        return lines

    def correction_bad_image(self, page):
        """
        [[file:Fifi-premier1.JPG|400px]]

        {{Fifi-premier1.JPG?400px}}
        """

        return page

class ConvertBatch(MyTools):

    def __init__(self):
        super().__init__()

        dire = "./output"
        master_dir = self.get_absolute_path_of_directory(dire)

        # Dict avec répertoires: liste des fichiers
        self.all_files = self.get_all_files(dire, ".mediawiki")

    def convert_all(self):

        for directory in self.all_files.keys():
            for page_file in self.all_files[directory]:
                #print("Conversion de ", page_file)
                conv = Convert(page_file)
                conv.convert()


def main():
    print("\nConversion:")
    convert = ConvertBatch()
    convert.convert_all()
    print("\nConversion terminée")

def test():
    page_file = ["./convert_test.mediawiki"]
    conv = Convert(page_file)
    conv.convert()
    data = conv.read_file("./convert_test.dokuwiki")


if __name__ == "__main__":

    main()
