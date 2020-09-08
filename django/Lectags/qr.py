import pyqrcode


class qr:


    def __init__(self):

        self.articulo = input('Lee lector qr')
        self.tmp = pyqrcode.QRCode( self.articulo, error='H', version=3, mode=None, encoding='iso-8859-1')
        #tmp = pyqrcode.create(articulo)
        #print(tmp.text())

        #enviar = input('Enviar linea S/N ' + articulo)
        #if(enviar == 'S' or enviar == 's'):
        print('Codigo enviado')
        self.tmp.show()
        self.lista =self.articulo.split('|')
    
    def getVal(self):
        return self.lista