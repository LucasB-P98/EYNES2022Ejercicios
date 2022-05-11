import doctest
import random
from operator import itemgetter

def create_lista_dic():
	'''
	This function creates and returns a list with dictionaries/persons with IDs in range 10 and randomized ages

	'''	
	list_dic=[]

	for i in range(10):
		auxiliar_dic={	'id':i+1,
						'age':random.randint(1,100)}
		list_dic.append(auxiliar_dic)

	return list_dic


def client_per_age(list_dic):
	'''
	This function receives a list and returns the same list but organized per age

	>>> client_per_age(list_dic= [{'id':4,'age':80}, {'id':1,'age':60}, {'id':8,'age':10}...])
	order_list[{'id':4,'age':80}, {'id':1,'age':60}, {'id':8,'age':10}...]
	'''
	order_list = sorted(list_dic, key=itemgetter('age'),reverse=True)

	return order_list

if __name__ == "__main__":
	my_list=create_lista_dic()
	my_list_size=len(my_list)

	print("Original list:\n\n"+str(my_list))

	my_list_per_Age=client_per_age(my_list)

	print("\n\nList per Age:\n\n"+str(my_list_per_Age))

	print("\n\nThe youngest person has the id: "+str(my_list_per_Age[my_list_size-1]['id']))
	print("The oldest person has the id: "+str(my_list_per_Age[my_list_size-my_list_size]['id'])+"\n")