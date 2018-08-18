string = raw_input("please enter string: ")
count = 0
if string.isdigit():
	print('integer')
	count+=1
elif type(string) == str:
	print('it is string')
	
