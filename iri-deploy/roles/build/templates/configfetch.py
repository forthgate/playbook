#!/usr/bin/env python
import os
import requests
import sys

file='/tmp/{{ app }}/config/development.json'
token = 'J3TvgxdsadfghwKCF2zj'
url = 'https://gitlab.example.com/api/v4/projects/118/repository/files/{{ env }}%2F{{ app }}%2Fapplication.yml/raw?ref=master'
page = requests.get(url, headers={'Private-Token': token })

print (page.text)
with open(file, 'w') as file:
     file.write(str(page.text))
     file.close()

