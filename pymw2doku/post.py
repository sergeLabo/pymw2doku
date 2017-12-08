#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests

##data = {"first_name":"Richard", "second_name":"Stallman"}
##r = requests.post("http://linuxfr.org", data = data)

##print(r.text)


r = requests.get('https://wiki.labomedia.org/index.php/Accueil', 
              auth=requests.auth.HTTPBasicAuth('serge', 'boubara1869'))
              
print(r.text)
