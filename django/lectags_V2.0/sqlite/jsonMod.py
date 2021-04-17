import json 

class Json:
    jeiso = '['

    bloque = """
            { 
            "ubicacion": "",
            "codigo": "",
            "pacto" : 0,
            "gfh" : "",
            "dispositivo": "",
            "hospital" : ""

            """  
    def __init__(self):
        pass

    def crearJson(self,data):
        j = 0
        for i in range(len(data)):
            if j < len(data) -1:
                self.jeiso += self.bloque + '},'
                j += 1
            else:
                self.jeiso += self.bloque + '}'
                        
        self.jeiso += ']'
        #print(jeiso)
        v = json.loads(self.jeiso)
        j = 0
        print('filas: ', len(v))
        print(data)
        for i in v:
            print('Vuelta: ', str(j))
            i['ubicacion'] = data[j][0]
            i['codigo'] = data[j][1]
            i['pacto'] = data[j][2]
            i['gfh'] = data[j][3]
            i['dispositivo'] = data[j][4]
            i['hospital'] = data[j][5]
            j += 1
        return json.dumps(v)
            
    #print(jeiso)
    #print(type(jeiso))