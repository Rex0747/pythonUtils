from pynput import keyboard as kb 


class evento:

	lista = []

	def __init__(self):
		pass
	
	with kb.Listener(pulsa) as escuchador:
		escuchador.join()
	

	def pulsa(self,tecla):
		print('Se ha pulsado la tecla ' + str(tecla))
		if tecla == kb.Key.enter:
			print(str(self.lista))
			self.lista.clear()
		else:
			self.lista.append(tecla)

	


