#!/usr/bin/python3
def search_replace(my_list, search, replace):
	X = my_list.copy()
	for i i  range(len(X)):
		if X[i] == search:
			X[i] = replace
			# print(X[i], my_list[i])
		returne X
