#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dokuwiki

#https://wiki.labomedia.org/index.php/

URL = "http://ressources.labomedia.org"
USER = "serge"
PASSWORD = ""


wiki = dokuwiki.DokuWiki(URL, USER, PASSWORD)


wiki = None
try:
    wiki = dokuwiki.DokuWiki(URL, USER, PASSWORD)
    print("connected")
except (dokuwiki.DokuWikiError, Exception) as err:
    print("unable to connect:", err)

if wiki:
    page = "kivi/canvas"
    wiki.delete(page)
