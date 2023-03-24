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

aux = r.text.split("\r\n")
print("Cantidad de mediciones: "+str(len(aux)-3))
medicion = aux[len(aux)-2].split()

print("Ultima medición "+str(medicion[0])+" a las "+str(medicion[1])+" hrs  \nLa temperatura actual es: " + str(medicion[2]) +"ºC")
#Hoy es 23/03/23 a las 20:50 hrs 

dia = medicion[0].split("/")
hora = medicion[1].split(":")

a = datetime.now() - datetime(int("20"+str(dia[2])), int(dia[1]), int(dia[0]), int(hora[0]), int(hora[1]), 0)

print("Hora actual: "+ str(datetime.now())+"\nDiferencia de "+ str(a))

if(int(str(a).split(":")[1]) > 5):
    print("Dato desactualizado")

