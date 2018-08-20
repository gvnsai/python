# Check input data is string or int or int in the string.

try:
    input_data=eval(input('Enter your input:'))
    if type(input_data) == int:
        print(input_data,' is int type')  
    elif type(input_data) == str:
        if input_data.isdigit():
            print(input_data,' is int in string')
        else:
            print(input_data,' is sting only')
except NameError:
    print('is string')
