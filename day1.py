#Problem 0 
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)
print(dates_of_birth)
#Problem 1
a = {"baak"}
b = {"dd"}
c = {"aa"}
x = set()
x = x.union(a, b, c)
print(x)
#Problem 2
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_2.difference(farm_1))
#Problem 3
set1 = {"bakai", 5, 3.5, True, (9)}
set1.add(25)
set2 = set1.copy()
set1.pop()
print(set2.difference(set1))
#Problem 4
menu = {
	'lagman': 120,
	'plov': '120', 
	'borsh': 100
}
menu.update({'drinks':['Cola','Sprite','Fanta']})
print(menu)
#Problem 020
set_methods = {'add','update','remove','clear','intersection','difference','discard','intersection_update','pop'}
dict_methods = {'clear','get','keys','values','items','update'}
x = dict_methods.intersection(set_methods)
print('Похожие методы: ',x)
#Problem 31
dict = {}
for c in range(0,3):
	login = str(input('login: '))
	password = str(input('password: '))
	dict.update({login:password})
print(dict)
#Problem 27
dict = {
	'bakai':'bilioner',
	'anton':'proggramer',
	'alibek':'taxi driver',
	'kumar':'buisnesess man',
	'bakyt':'president',
}
names = list(dict.keys())
jobs = list(dict.values())
for x in range(5):
	print("Здравствуйте", names[x],'Прекрасная профессия', jobs[x])
#Problem 22
numbers = set()
for x in range(10):
	num = int(input('number: '))
	numbers.add(num)
result = tuple(numbers)
print(result)
#Problem 99
menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
menu.update({'besh_barmak': 130})
menu['besh_barmak'] = 135
del menu['borsh']
print('Обновленное меню: ',menu)
#Problem 11
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
new = set(south_american_countries)
print('Без дублированных элементов: ',new)
#Problem 101
suitcase = []
for x in range(5):
	items = input('Что возбмем собой?')
	suitcase.append(items)
suitcase.pop(4)
print('Чемоданчик: ', suitcase)
#Problem 001
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
intersection_set = farm_1.intersection(farm_2)
difference_set = farm_1.difference(farm_2)
print(intersection_set)
print(difference_set)
