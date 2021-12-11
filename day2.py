##1
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
lang = input('language: ')
if lang in languages:
	print('this langiage in the list')
else:
	pass
#2
for words in languages:
	if words == 'php':
		break
	print(words)
#3
num = 7
for x in range(5):
	num *= num
print(num)
#4
for x in range(len(languages)):
	print(x,languages[x])
#5
y = 10
for x in range(1,20):
	if x < 11:
		print(x)
	elif x > 10:
		y -= 1
		print(y)
#6
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
lst_names = list(names)
print(lst_names[2::2])
#7
print(lst_names[::2])
#8
#1.Это число трёхзначное?
#2.Это число положительное и чётное?
#3.Это число делится на 31 без остатка?
#4.Если это число больше 100 и оно делится на 17 без остатка или это число больше 150 и равно 13**2 тогда показать что это за число
num = int(input('input number!: '))
str_num = str(num)
if len(str_num) == 3:
	print('Трехзначенное число!')
if num%2 == 0:
	print('Число четное!')
if num%3 == 0 or num == 1:
	print('Число не четное!')
if (num > 100 and num % 17 == 0) or (num > 150 and num == 13**2):
	print('Число выполнило 4 условие!', num)
#9
numbers = [range(-100,100)]
a = 0
b = 0
a_list = []
b_list = []
for x in range(-100,100):
	if x % 13 == 0 and x % 2 == 0:
		a_list.append(x**2)
		a += 1
	if x % 7 == 0 and x % 2 != 0:
		b_list.append(x)
		b += 1
print(a,'Числ подходят под первое условие!', b, 'Подходит под второе условие!')
print(a_list)
print(b_list)


