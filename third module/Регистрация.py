import json
login = input('Введите логин: ')
passwd = input('Введите пароль: ')
def register(login, passwd):
	pass
data = login, passwd	
with open('5.json', 'a') as f:
	json.dump(data, f)
print('Ваш логин: ', login)
print('Ваш пароль: ', passwd)