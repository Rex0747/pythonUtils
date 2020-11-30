import requests
from sqlite.jsonMod import Json


#resp = requests.get('http://localhost:8082/etiquetas/2118')

mtx = (('2','4','7','1','98988','20.0','H7NA','IZ034','HCSC'),('3','1','2','1','011334','1.0','H7NA','IZL024','HCSC'))

joson = Json()

v1 = joson.crearJson(mtx)
print('JSON: ', v1)
