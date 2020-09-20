import requests
import json

resp = requests.get('http://localhost:8082/etiquetas/2118')

print( resp.ok )
#print(type(resp))
if resp.ok == True:
	
