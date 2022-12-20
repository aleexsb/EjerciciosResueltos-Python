#SUBIR UN TEXTO A PASTEBIN Y HACER UN PROGRAMA QUE LO BAJE
import requests

import logging,time
logging.basicConfig(filename='requestsLog',level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

url = 'https://pastebin.com/raw/uvBhLZpd'
res = requests.get(url)

try:
	res.raise_for_status()
	archivoBinario = open('pastebin.txt', 'wb')
	for chunk in res.iter_content(100000):
		archivoBinario.write(chunk)
	archivoBinario.close()
except:
	print('No funciona el pastebin')
