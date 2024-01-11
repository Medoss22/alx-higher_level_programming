#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	X = []
	for i in matrix:
		X_i = []
		for j in i:
			X_i.append(j ** 2)
		X.append(X_i)
	return X
