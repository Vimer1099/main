name = input("Введите ваше имя: ")
print("Добро Пожаловать: " + name)
if name == '1", "2", "3", "4", "5", "6", "7", "8","9","10':
			 raise ZeroDivisionError
	except ValueError:
		print('Wrong value')
  except ZeroDivisionError:
		name = ''
		print('Please write your name')

num1 = num2 = sign = ''
while num1 == '' or num2 == '' or sign == '':
	try:
		num1 = int(input('Number1: '))
		sign = input('Sign: ')
		num2 = int(input('Number2: '))
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