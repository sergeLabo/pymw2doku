#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
convertit le code en doku
"""


import re
import pypandoc

PARAGRAPH = """
=rien 1=
==test 2==
===test 3 totgdfg gdf===
====test 4 sdfhfh dfgdf ====
=====test 5 hgf rtyrt =====
"""

FILE = """

[[Image:ResizePersonnage10.png]]
[[Fichier:ResizePersonnage10.png]]
[[File:ResizePersonnage10.png]]

"""


class MwToDoku:
    def __init__(self, page):
        self.page = page

    def get_doku(self):
        """Substitution de mw par syntaxe doku"""

        lines = ""
        page_list = self.page.split('\n')
        for line in page_list:
            line = re.sub(r"^[\t\f ]*=([^=]+?)=[\t\f ]*$", "====\\1====", line, count=0,flags=re.M)
            line = re.sub(r"^[\t\f ]*==([^=]+?)==[\t\f ]*$", "===\\1===", line, count=0,flags=re.M)
            line = re.sub(r"^[\t\f ]*===([^=]+?)===[\t\f ]*$", "==\\1==", line, count=0,flags=re.M)
            line = re.sub(r"^[\t\f ]*====([^=]+?)====[\t\f ]*$", "=\\1=", line, count=0,flags=re.M)
            line = re.sub(r"^[\t\f ]*=====([^=]+?)=====[\t\f ]*$", "**\\1**", line, count=0,flags=re.M)
            lines = lines + line + "\n"
        return lines
        

def test():
    mwtodoku = MwToDoku(PARAGRAPH)
    lines = mwtodoku.get_doku()
    print(PARAGRAPH)
    print(lines)
    
def test1():
    output = pypandoc.convert_file( './Gif_anim.mediawiki', 
                                    'dokuwiki', 
                                    outputfile='./Gif_anim.dokuwiki')
    
if __name__ == "__main__":
    #test1()
    test()
