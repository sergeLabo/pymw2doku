#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Conversion du 
code mediawiki
en
code dokuwiki

Bon ! Faut pas rêver, ce script fait les choses:
* possibles
* faciles

Liste des fonctionnalités:
* paragraphe  = to =====
* category to tag
* liste * to __*
* lien mw to lien doku
* syntax fichiers, images 
* syntax video
* syntaxhighlight

"""

import re
from my_tools import MyTools 

class Conversion:
    
    def __init__(self, file_name):
        """file_name avec chemin depuis le dossier de ce script"""
        
        pass
       
def list_conversion(line):
    
    re.sub("*", "  *")
        
def test1():
    line = "* ma liste"
    line = list_conversion(line)
    print(line)
    
formatter = {   "''"  : "//",  # italics
                    "'''" : "**"}  # boldface
               
def test2():               
    mt = MyTools()
    file_name
    mt.read_file(file_name)  
                    
if __name__ == '__main__':
    test2()
