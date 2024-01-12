#!/usr/bin/python3
def uniq_add(my_list=[]):
	R = 0
	new = set(my_list)
	for num in new:
		R += num
		# to new if num duplicate or not and result -> print(num, Result)
	return R
