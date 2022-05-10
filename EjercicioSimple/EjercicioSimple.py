import doctest
import random
from operator import itemgetter

def lista_dic():
	listadic=[
		{
			'id':1,
			'edad':random.randint(1,100)
		},
		{
			'id':2,
			'edad':random.randint(1,100)
		},
		{
			'id':3,
			'edad':random.randint(1,100)
		},
		{
			'id':4,
			'edad':random.randint(1,100)
		},
		{
			'id':5,
			'edad':random.randint(1,100)
		},
		{
			'id':6,
			'edad':random.randint(1,100)
		},
		{
			'id':7,
			'edad':random.randint(1,100)
		},
		{
			'id':8,
			'edad':random.randint(1,100)
		},
		{
			'id':9,
			'edad':random.randint(1,100)
		},
		{
			'id':10,
			'edad':random.randint(1,100)
		},
]
	return listadic


def ordenar_clientes_edad(lista):

	lista_ordenada = sorted(lista, key=itemgetter('edad'),reverse=True)

	print("La persona mas joven tiene la id: "+str(lista_ordenada[9]['id']))
	print("La persona mas vieja tiene la id: "+str(lista_ordenada[0]['id']))

	return lista_ordenada
