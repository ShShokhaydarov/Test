# x = {'name':'Pasha', 'Job': 'Tgbor cereator'}
# print(x['name'])
#
# x = {'name':'Pasha', 'Job': 'Tgbor cereator'}
# print(x['name'], x['Job'])
#
# date = {'name': ['Jordan', 'Pavel'],
#         'age': (12, 21),
#         'job': 'programmes'}
#
# print(date['name'][0], date['job'][-1])
#
# x = input('Введи имя пожалуйста..: ')
# y = {'name': x,
#      'course': 'Pyhton developer'}
# print(y['name'], y['course'])
# ?
# def creat_list():
#     my_list = []
#     return my_list
#
# def spam2(4):
#     print(a + 6)
#     spam2(3)
#
# def x(a, b):
#     return a / b
#
# print(x(100, 2))
#
# def x(a, b):
#     return a * b
#
# print(x(100, 2))
#
# def x(a, b):
#     return a % b
#
# print(x(100, 2))
#
# allproducts = {'Склад': {'name': 'Хлеб', 'количество' : 34}}
#
# def get_products(a='name'):
#     print((allproducts['Склад'][a]))
# get_products()
#
# def spam1(*args):
#     return args
# print(spam1(1,2,3, 'Hello'))
#
# def spam1(*blabla):
#     print(sum(blabla))
#
# print(spam1(1,2,3,4,5,6))
#
# def spam1(**blabla):
#     return blabla
# print(spam1(name='my1', num=23))
#
# clienst = []
# rooms = [for my in range(1,21)]
# busyrooms = []
#
# print('Добавить', 'Удалить клиента', 'Увидеть свободные номера ')
# choice = input('Что ты хочешь? ')
#     if x == 'Добавить':
#         clienst = input('Введи имя клиента')
#         rooms = input('Введите номер в отеле')
#
# a = lambda x: x**2
# print(a(10))
#
# x = lambda b, a: b**8 + a**5
# print(x(6, 9))
#
# Sh = lambda a, b, c: a**2 + b**3 + c
# print(Sh(2, 4, 6)
#
# import requests
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
# link = 'https://httpbin.org/post'
#
# data = {'custname': 'Aziz',
#         'custtel': '+9989000000000',
#         'custemail': 'elon@mail.com',
#         'size': 'small',
#         'topping': 'cheese',
#         'delivery': '20:00',
#         'comments': 'asdasd'}
# print(requests.post(url=link, headers=headers, params=data).text)
#
# class User:
#     name = 'Jordan'
#
# class Car:
#     type = 'Bugatti'
#     color = 'white'
#     max_speed = 300
#
# class Person:
#     name = 'Jordan'
#     age = 23
#     job = 'programmer'
#
# class human:
#     pass
#
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# gentra = Car('Chervrolet', 'Black', 2021)
# print(gentra.year)
# print(gentra.model)
# print(gentra.color)

# class Comment:
#     def __init__(self, user, text, likes):
#         self.user = user
#         self.text = text
#         self.likes = likes
# comments = Comment('Shoaziz', 'Отличный курс', 5)
# print(comments.user, comments.text, comments.likes)

# class BankAccount:
#     def __init__(self, user, user_b):
#     self.user = user
#     self.user_b - user_b

# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
# class Bank_Account:
#     def __init__(self):
# 	    self.balance=0
#         print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
#
#     def deposit(self):
#         amount=float(input("Enter amount to be Deposited: "))
# 		self.balance += amount
# 		print("\n Amount Deposited:",amount)
#
#     def withdraw(self):
# 		amount = float(input("Enter amount to be Withdrawn: "))
# 		if self.balance>=amount:
# 			self.balance-=amount
# 			print("\n You Withdrew:", amount)
# 		else:
# 			print("\n Insufficient balance ")
#
# def display(self):
# 		print("\n Net Available Balance=",self.balance)
#
# # Driver code
#
# # creating an object of class
# s = Bank_Account()
#
# # Calling functions with that class object
# s.deposit()
# s.withdraw()
# s.display()

# class BankAccount:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def cash(self, amount):
#         self.balance(self):
#     def my_balance(self, amount):
#         return self.balance
#


# Гит хаб проект для соеденине команды Teamпше

