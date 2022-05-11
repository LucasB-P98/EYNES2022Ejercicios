import numpy as np
import doctest
import turtle


def circle_multiplication(circle,value):
		'''
		Testing circle_multiplication function
		>>> circle_multiplication(circle,3)
		Function returns a new Circle object
		>>> circle_multiplication(circle,-3)
		Exception throw. Invalid multiplication
		'''
		if value<=0:
			raise ValueError("The radius cannot be: {}".format(radius))
		new_circle=Circle(circle.get_radius()*value)
		return new_circle


class Circle():

	def __init__(self,radius):
		'''
		Testing the Circle 
		>>> __init__(self,10)
		Valid object
		>>> __init__(self,-3)
		Exception throw. Invalid object
		'''
		if radius<=0:
			raise ValueError("The radius cannot be: {}".format(radius))
		self.__radius=radius
	def get_radius(self):
		return self.__radius

	def get_area(self):

		return (3.14159*(self.__radius**2))

	def get_perimeter(self):
		return ((2*3.14159)*self.__radius)

	def set_radius(radius):
		'''
		Testing set_radius method 
		>>> set_radius(10)
		self.__radius=10
		>>> __init__(self,-3)
		Exception throw. Invalid modification
		'''
		if radius<=0:
			raise ValueError("The radius cannot be: {}".format(radius))
		self.__radius=radius

	
	def __repr__(self):
		temporaryRepr= turtle.Turtle()
		temporaryRepr.circle(self.__radius)

		return "El radio del circulo es: "+str(self.__radius)

if __name__=="__main__":


	my_circle=Circle(11)
	print(my_circle)

	my_second_circle=circle_multiplication(my_circle,4)


