#1
#a = ['bakai','ergeshev',('lol'),(255),55,{'four':4}]
#cheak = []
#for x in a:
#	try:
#		s = set(x)
#		cheak.append(True)
#	except TypeError:
#		cheak.append(False)
#if all(cheak) == True:
#	print('Данные можно конвертировать в Set')
#elif all(cheak) == False:
#	print('Данные нельзя конвертировать в Set')
#2
#numbers = set()
#for x in range(5):
#	num = int(input('num: '))
#	numbers.add(num)
#print(min(numbers))
#3
#function = input(''' ''')
#try:
#	eval(function)
#except:
#	print('Wrong')
#else:
#	print('Correct')

#4
credit = int(input('Сколько хотите взять в кредит?'))
result = credit * (3.47/100)
#print('Переплата составила: ',round(result,2))

#1 and 2
a = ['bakai',10]
#try:
#	x = set(a)
#	b = set(a[2])
#	с = lol
#	except TypeError:
#		print('Нельзя конвертировать в СЕТ')
#	except IndexError:
#		print('Индекс вышел за предел')
#	except NameError:
#		print('Нету такого обьекта')
#3 and 4
a[1] = str(a[1])
a.append({'dict': 1})
lol = 20
c = lol
x = set(a)
print(x)
print(a[2])
print(c)
#
