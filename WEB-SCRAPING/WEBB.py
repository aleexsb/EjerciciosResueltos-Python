#DESCARGAR LA TEMPERATURA DE UNA PAGINA WEB 

import requests,bs4,logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

url = 'https://weather.com/weather/today/l/Buenos+Aires+Argentina+ARBA0009:1:AR'
respuesta = requests.get(url)
sopa = bs4.BeautifulSoup(respuesta.text,'html.parser')
resultados = sopa.select('#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div.CurrentConditions--body--8sQIV > div.CurrentConditions--columns--3KgfN > div.CurrentConditions--primary--2SVPh > span') #ESTE TAG LARGO VA CAMBIANDO HAY QUE ENTRAR Y FIGARSE DE NUEVO COMO ESTA ACTUALIZADO

temperatura = resultados[0].getText()
print(f'Temperatura en Buenos Aires: {temperatura}(en Farenheit)')