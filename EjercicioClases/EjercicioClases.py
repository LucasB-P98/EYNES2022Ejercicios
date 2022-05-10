import numpy as np

class ExcepcionRadioCirculo(Exception):

	def __init__(self,circulo,mensaje):
		super(ExcepcionRadioCirculo,self).__init__(mensaje)


class Circulo():
	def __init__(self,radio):
			
		try:
			if radio<=0:
				raise ExcepcionRadioCirculo(self,'El radio no puede ser <=0')
			self.__radio=radio
		except ExcepcionRadioCirculo as e:
			print(e)

	def get_radio():
		return self.__radio

	def get_area():
		return np.pi()*(self.__radio**2)

	def get_perimetro():
		return (2*np.pi())*self.__radio

	def set_radio(radio):
		self.__radio=radio
	
	def multiplicar_circulo(circulo,valor):
		nuevo_circulo=Circulo(circulo.set_radio()*valor)

		return nuevo_circulo

if __name__=="__main__":

	mi_circulo=Circulo(-3)

