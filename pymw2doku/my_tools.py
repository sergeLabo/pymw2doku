#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from pathlib import Path
from json import dumps, loads

"""Des méthodes souvent appelées par les autres scripts."""


class MyTools:

    def get_all_files(self, master_dir, file_end):
        """Retourne un dict avec
        clé = répertoires
        valeur = liste de tous les fichiers avec chemin relatif
        dict = {    "2017_06": [/abs/meteo_x0.html, /abs/meteo_x1.html .....],
                    "2017_07": [/abs/meteo_y0.html, /abs/meteo_y1.html .....],}

        master_dir = répertoire dans le dossier de ce script
        file_end = ".txt" ou ".html" ou ...
        """

        all_files = {}

        for directory in os.listdir(master_dir):
            all_files[directory] = []
            for fichier in os.listdir(master_dir + "/" + directory):
                #print("Fichier trouvé:", directory, fichier)
                if fichier.endswith(file_end):
                    file_name = os.path.join(fichier)
                    abs_file = master_dir + "/" + directory + "/" + file_name
                    all_files[directory].append(abs_file)

        return all_files

    def read_file(self, file_name):
        """Retourne les datas lues dans le fichier avec son chemin/nom
        Retourne None si fichier inexistant ou impossible à lire .
        """

        try:
            with open(file_name) as f:
                data = f.read()
            f.close()
        except:
            data = None
            print("Fichier inexistant ou impossible à lire:", file_name)

        return data

    def write_data_in_file(self, data, fichier):
        """Ecrit les data dans le fichier, écrase l'existant."""

        with open(fichier, 'w') as fd:
            fd.write(data)
        fd.close()

    def data_to_json(self, data):
        """Retourne le json des datas"""

        return dumps(data)

    def get_json_file(self, fichier):
        """Retourne le json décodé des datas lues
        dans le fichier avec son chemin/nom.
        """

        # Open our local file
        with open(fichier) as f:
            data = f.read()
        f.close()

        data = loads(data)

        return data

    def print_all_key_value(self, my_dict):
        """Imprime un dict contenant un dict,
        affiche le nombre de clés total.
        """

        total = 0

        for k, v in my_dict.items():
            print(k)
            for f in v:
                total += 1
                print("    ", f)
        print("Nombre de clés total =", total)
        print("pour un théorique par jour de =", 24*1)

    def create_directory(self, directory):
        """Crée le répertoire avec le chemin absolu.
        ex: /media/data/3D/projets/meteo/meteo_forecast/2017_06
        """

        try:
            Path(directory).mkdir(mode=0o777, parents=False)
            print("Création du répertoire: {}".format(directory))
        except FileExistsError as e:
            pass

    def get_absolute_path(self, a_file_or_a_directory):
        """Retourne le chemin absolu d'un répertoire ou d'un fichier
        n'importe où.
        """

        return os.path.abspath(a_file_or_a_directory)


def test0():
    pass


if __name__ == "__main__":

    test0()
