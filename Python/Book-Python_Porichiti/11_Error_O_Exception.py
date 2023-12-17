## BOOK: Python Porichiti - Chapter 11


]def divide(a,b):
	return a / b


a = 5
b = 3

print(divide(a,b))

def divide2(a,b):
	try:
		result = a / b
	except ZeroDivisionError:
		print('you cant divide by zero')
	except TypeError:
		print('Data Type Not Supported')
	else:
		return result
		
		
		
a = 2
b = '3'

print(divide2(a,b))


def divide3(a,b):
	try:
		result = a / b
	except ZeroDivisionError:
		print('You can\'t Divide By Zero')
	except TypeError:
		print("Data Type Not Supported")
	else:
		return result
	finally:
		print('Inside Finally')

c = 6
d = 0

print(divide3(c,d))

#------------

for i in range(10):
	print(i)
	break
else:
	print('Inside Else')
	
#--------------------


for i in range(10):
	print(i)
	try:
		print('lol')
	except StopIteration:
		print('You can\'t use Except')
