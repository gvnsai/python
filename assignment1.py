string = raw_input("please enter string: ")
count = 0
if string.isdigit():
	print('integer')
	count+=1
elif type(string) == str:
	print('it is string')
	# new_str = string.split(' ')
	# for i in new_str:
	# 	if i.isdigit():
	# 		print('integer in the string')
	# 		count+= 1
	# 		break
	# 	else:
	# 		pass
# if count==1:
# 	print('it is a int')