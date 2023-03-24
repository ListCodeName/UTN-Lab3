"""
Para el correcto funcionamiento de este algoritmo se requiere tener la libreria 'requests':

pip install requests

"""

import requests
from datetime import datetime

r = requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')

#print(r.headers)
#print (r.status_code)
#print(r.encoding)
#print(r.content)

#Obtener la temperatura y la fecha de la ultima medición
aux = r.text.split("\r\n")
print("\nCantidad de mediciones: "+str(len(aux)-4))
medicion = aux[len(aux)-2].split()

print("\nUltima medición "+str(medicion[0])+" a las "+str(medicion[1])+" hrs  \nLa temperatura actual es: " + str(medicion[2]) +"ºC")

#Calculo del tiempo transcurrido desde la ultima medición y la fecha actual 
dia = medicion[0].split("/")
hora = medicion[1].split(":")

a = datetime.now() - datetime(int("20"+str(dia[2])), int(dia[1]), int(dia[0]), int(hora[0]), int(hora[1]), 0)
print("\nHora actual: "+ str(datetime.now())+"\nDiferencia de "+ str(a))

#En caso de que los minutos pasados de la ultima medición sean mayor a 5 se mostrará un mensaje
if(int(str(a).split(":")[1]) > 5):
    print("\nDato desactualizado")

#Obtener media, máxima y mínima de temperaturas registradas
media, max, min, cont = 0,0,0,0
current = ""
for x in aux:
    if(cont < 3):
        cont +=1
        continue
    try:
        current = x.split()[2]
        media += float(current)
        if(min > float(current) or min == 0):
            min = float(current)
        if(max < float(current) or min == 0):
            max = float(current)
    except:
        print("\n")
print("Temperatura máxima: "+str(max)+"\nTemperatura mínima: "+str(min)+"\nTemperatura media: "+str(media/(len(aux)-4)))
