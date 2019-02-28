#!/usr/bin/env python
import os
import requests
import sys

file='config/production.json'
token = 'J3TvgxJwe3Ld1wKCF2zj'
url = 'https://gitlab.example.com/conf/configs/raw/master/iri-stage/"{{ app }}"/application.yml'
page = requests.get(url, headers={'Private-Token': token })

print (page.text)
with open(file, 'w') as file:
     file.write(str(page.text))
     file.close()

