# ##1
# x = '''bin@ dev/ lib@ libx32@ mnt/ root/ snap/ sys/ var/ boot/ etc/ lib32@ lost+found/ opt/ run/ srv/ tmp/
# cdrom/ home/ lib64@ media/ proc/ sbin@ swapfile usr/'''
#
# file = open('directories.txt', 'w')
# file.write(x)
# file.close()
# file2 = open('directories.txt', 'r')
# print(file2.read())
# file2.close()

#2

# users = open('users.txt', 'w')
# login = input('login: ')
# password = input('password: ')
# users.write(f'login: {login}')
# users.write(f' password: {password}')
# users.close()
# users2 = open('users.txt', 'r')
# print(users2.read())
# users2.close()

#3

# w = open('w.txt', 'w')
# w.write('kaswwasdasfdwww')
# w.close()
# w1 = open('w.txt', 'r')
# if 'w' in w1.read():
# 	print('"w" есть в тексте')
# else:
# 	print('"w" нету в тексте')
# w1.close()


#4

# text = open('python.txt', 'w')
# text.write(''' Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords) and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java.''')
# text.close()
# t_words = []
#
# with open('python.txt', 'r') as f:
# 	lst = f.read()
# 	a = lst.split(' ')
# 	for x in a:
# 		if ('t' or 'T') in x:
# 			t_words.append(x)
# 	print(t_words)

#1

# with open('database.txt', 'w') as data:
# 	input_dict = '''['julka' : 12345, 'yo' : 54321, 'lox' ; 'lol']'''
# 	data.write(input_dict)
with open('database.txt', 'r') as data_r:
	x = dict(data_r.read())
	choose = int(input
	('''
	1 : Зарегистрироваться
	2 : Войти
	'''))
	if choose == 1:
		login = input('Input Login: ')
		while login in x.keys():
			print('This login is taken, please change login!')
			login = input('Input Login')
		password = input('Input password: ')
		print('succefully registrated')
	elif choose == 2:
		login = input('Input login')
		while login not in x.keys():
			print('There is no such a login, please registrate')
			login = input('Input login: ')
		password = input('Password: ')
		while password not in x.values() and login in x.values():
			print('password is wrong')
			password = input('Password: ')
		print('succefully signed in')






