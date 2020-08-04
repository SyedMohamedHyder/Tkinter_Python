#!/c/Users/SYED/AppData/Local/Programs/Python/Python38-32/python

import string

def convert_to_base(n,b):

	if b <2 :

		return ValueError("Base must be atleast greater than 2")

	if n == 0:

		return [0]

	result=[]

	while n > 0: 

		n,mod=divmod(n,b)

		result.insert(0,mod)

	return result

def correct_num(num_list,num_map):

	if len(num_map) > max(num_list):

		return "".join(num_map[num] for num in num_list)

	else:

		raise ValueError("Map is not long enough")

def rebase_number(num,base):

	positive = False if num < 0 else True

	conversion_map = "0123456789"+string.ascii_letters.upper()

	result = convert_to_base(num,base)

	answer = correct_num(result,conversion_map)

	answer = answer if positive else "-{0}".format(answer)

	return answer

print (rebase_number(16,16))
