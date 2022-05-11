import numpy as np
import random


def matrix_creation(row,col):
	return [[random.randint(1,10)for j in range(col)]for i in range(row)]


if __name__ == "__main__":

	matrix=matrix_creation(5,5)

	print("Original Matrix")

	for row in matrix:
		print(row)

	i=0
	j=0

	
	consecutive_sequence_horizontal=0
	consecutive_sequence_vertical=0

	for i in range(len(matrix)):
		print(matrix[i][j])
		for j in range(len(matrix)):
			pass

	print("The vertical consecutive numbers sequence is: "+str(consecutive_sequence_vertical))



			






