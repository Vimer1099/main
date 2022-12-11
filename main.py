# def sad(func):
# 	def wrapper():
# 		func()
# 		print('he is sad')
# 	return wrapper
# @sad
  
# def human():
# 	print('this is human')

# human()

# --------------------------------------------------------
def AI():
  print('Hello, Im Robot Calculator!')

AI();

name = input("Enter your username: ")
print("Welcome: " + name)
# if name == '1", "2", "3", "4", "5", "6", "7", "8","9","10':
# 			 raise ZeroDivisionError
# 	except ValueError:
# 		print('Wrong value')
#   except ZeroDivisionError:
# 		name = ''
# 		print('Please write your name')

num1 = num2 = sign = ''
while num1 == '' or num2 == '' or sign == '':
	try:
		num1 = int(input('Number 1: '))
		sign = input('Sign: ')
		num2 = int(input('Number 2: '))
		if sign == '/' and num2 == 0:
			raise ZeroDivisionError
	except ValueError:
		print('Wrong value')
	except ZeroDivisionError:
		sign = ''
		print('Go to school')
	except:
		print('Something go wrong')
	try:
		if sign == '+':
			print(f"{num1} + {num2} = {num1+num2}")
		elif sign == '-':
			print(f"{num1} - {num2} = {num1-num2}")
		elif sign == '/':
			print(f"{num1} / {num2} = {num1/num2}")
	except TypeError:
		print('Wrong types')


# ----------------------------------------

# def timer(func):
# 	import time
# 	def wrapper():
# 		start = time.time()
# 		func()
# 		end = time.time()
# 		print('time: ', end-start)
# 	return wrapper

# count = 0
# def counter(func):
# 	def wrapper():
# 		global count
# 		count+=1
# 		func()
# 		print(func.__name__, 'is called', count)
# 	return wrapper

# def logging(func):
# 	def wrapper():
# 		func()
# 		print('Function is',func.__name__)
# 	return wrapper

# @logging
# @counter
# @timer
# def webpage():
# 	import requests
# 	page = requests.get('https://www.random.org/')
# 	print(page.text)

# @counter
# @timer
# def ask():
# 	a = input('Text: ')
# 	print(a)

# ask()

# -----------------------------------