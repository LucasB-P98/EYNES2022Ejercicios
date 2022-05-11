import numpy as np
import random
import doctest


def matrix_creation(row,col):
	'''
	Matrix creation function returns a matrix

	>>> matrix_creation(3,3)
	[[2,4,7]
 	[5,7,2]
 	[4,10,3]
	 [1,8,8]]
 	>>> matrix_creation(0,0)
	 []
	 >>> matrix_creation(a,b)
 	NameError

	'''
	return [[random.randint(1,10)for j in range(col)]for i in range(row)]


if __name__ == "__main__":

	matrix=matrix_creation(5,5)

	print("-Original Matrix-\n")

	print(np.transpose(matrix))

	found_initial_position=0
	found_final_position=0
	consecutive_sequence=0

	i=0
	j=0

	for i in range(len(matrix)):
		
		for j in range(len(matrix)-1):
			if ((matrix[i][j]-matrix[i][j+1])== 1 or (matrix[i][j]-matrix[i][j+1])== -1):
				if consecutive_sequence==0:
					found_initial_position=(i,j)
				consecutive_sequence+=1
				found_final_position=(i,j)

	print("\nThe consecutive numbers sequence is: "+str(consecutive_sequence)+" \nInitial position at: "+str(found_initial_position)+"\nFinal position at : "+str(found_final_position))



			






