import numpy as np
import doctest


class Circle():
	def __init__(self,radius):
		if radius<=0:
			raise ValueError("The radius cannot be: {}".format(radius))
		self.__radius=radius
	def get_radius():
		return self.__radius

	def get_area():
		return np.pi()*(self.__radius**2)

	def get_perimeter():
		return (2*np.pi())*self.__radius

	def set_radius(radius):
		if radius<=0:
			raise ValueError("The radius cannot be: {}".format(radius))
		self.__radius=radius
	
	def circle_multiplication(circle,radius):
		if value<=0:
			raise ValueError("The radius cannot be: {}".format(radius))
		new_circle=Circle(circle.set_radius()*value)

		return new_circle

if __name__=="__main__":

	my_circle=Circle(3)

