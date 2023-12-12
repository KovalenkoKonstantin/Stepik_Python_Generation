# print("Мы изучаем язык Python")
# print("Python")
# print("Python")
# print("Скоро я", "буду программировать", "на языке", "Python!", sep="-")
# print('Какой хороший день!')
# print('Работать мне не лень!')
# print('Какой хороший день!')
# print()
# print('Работать мне не лень!')
# print('В тексте есть "двойные" кавычки')
# print("В тексте есть 'одинарные' кавычки")
# print(4, 8, 15, 16, 23, 42, sep='\n')
# print('*', '**', '***', '****', '*****', '******', '*******', sep='\n')
# print('Как тебя зовут?')
# name = input()
# print('Привет,', name)
# # сначала тут печатается строка "Как тебя зовут", а потом принимается на вход имя
# name = input('Как тебя зовут?'+'\n')
#
# # тут просто выводится строка "Привет", после неё идёт пробел и введённое нами имя
# print('Привет,', name)
# n = input()
# print('Привет,', input())
# print(input(), '- чемпион!')
# print(input(), input(), input(), sep='\n')
# a = input()
# b = input()
# c = input()
# print(c, b, a, sep='\n')
# print(*reversed([input(), input(), input()]), sep="\n")
# a, b, c = input(), input(), input()
# print(c, b, a, sep="\n")
# print('a', 'b', 'c', end='@')
# print('d', 'e', 'f', end='@@')
# print('a', 'b', 'c', sep='*', end='finish')
# print('d', 'e', 'f', sep='**', end='^__^')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='#')
# print('m', 'n', 'o', sep='/', end='!')
# print('31', '12', '2019', sep='-')
# print('Mercury', 'Venus', sep='*', end='!')
# print('Mars', 'Jupiter', sep='**', end='?')
# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')
# print('I***like***Python')
# a = input()
# print(input(), input(), input(), sep=a)
# print('Привет, ', input(), '!', sep='')
# variable_name = input()
# print('Вы ввели текст:', variable_name)
# print('Как тебя зовут?')
# name = input()
# print('Привет,', name)
# name = 'Timur'
# print('Привет,', name)
# name, surname = 'Timur', 'Guev'
# print('Имя:', name, 'Фамилия:', surname)
# language = 'Python'
# language = 'Pascal'
# print(language)
# s1 = 'C++'
# s2 = 'Python'
# s3 = 'Java'
# s3 = s2
# s1 = s3
# print(s1)
# print('Java')
# print('Ruby')
# print('Scala')
# print('Python', end='+')  # print('C++')
# # print('GO')
# print('C#', end='=')  # print('C')
# print('awesome')
# finish
# num = 7
# num1 = 10
# num2 = num + num1
# print(num2)
# s = 0
# k = 30
# d = k - 5
# k = 2 * d
# s = k - 100
# print(s)
# x = 3
# y = 4
# z = x + y
# z = z + 1
# x = y
# y = 5
# x = z + y + 7
# print(x)
# a = 4
# print(a, "a")
# a = int(input())
# print(a)
# print(a + 1)
# print(a + 2)
# print(int(input()) + int(input()) + int(input()))
# a = int(input())
# print('Объём = ' + str(pow(a, 3)))
# print('Площадь полной поверхности = ' + str(6 * pow(a, 2)))
# a, b = int(input()), int(input())
# print(3 * pow((a + b), 3) + 275 * pow(b, 2) - 127 * a - 41)
# x = int(input())
# print('Следующее за числом ', x, ' число: ', x+1, '\n',
#       'Для числа ', x, ' предыдущее число: ', x-1, sep='')
# print(2 ** 0)
# print(2 ** 1)
# print(2 ** 2)
# print(2 ** 3)
# print(2 ** (-1))
# print(2 ** 2 ** 3)
# print(10 // 3) # округление в меньшую сторону
# print(-10 // 3) # округление в меньшую сторону
# Обратите внимание: 
# результатом деления n % m при n < m является число n. 
# Например, 5 % 9 = 5, 3 % 13 = 3 и т.д.
# print(23//7)
# print(20//5)
# print(2//5)
# print(123//10)
# print(-123//10)
# print(23 % 7)
# print(20 % 5)
# print(2 % 5)
# print(123 % 10)
# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)
# a = 82 // 3 ** 2 % 7
# print(a)
# b, q, n = int(input()), int(input()), int(input())
# print(b * q ** (n - 1))
# print(int(input()) // 100)
# n, k, = int(input()), int(input())
# print(k // n, k % n, sep='\n')
# from math import ceil
#
# n = int(input())
# print(ceil(n/2))
# print(n // 2 + n % 2)
# from math import ceil
# print(ceil(int(input())/4))
# x = int(input())
# print(x, ' мин - это ', x // 60, ' час ', x % 60, ' минут.', sep='')
# num = int(input())
# a = num % 10
# b = (num % 100) // 10
# c = num // 100
#
# print('Сумма цифр = ', a + b + c, sep='')
# print('Произведение цифр = ', a * b * c, sep='')
# num = int(input())
# c = num % 10
# b = (num % 100) // 10
# a = num // 100
# print(a, b, c, sep='')
# print(a, c, b, sep='')
# print(b, a, c, sep='')
# print(b, c, a, sep='')
# print(c, a, b, sep='')
# print(c, b, a, sep='')

# a, b, c = input()
# print(a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a, sep='\n')
# a, b, c, d = input()
# print('Цифра в позиции тысяч равна ' + a)
# print('Цифра в позиции сотен равна ' + b)
# print('Цифра в позиции десятков равна ' + c)
# print('Цифра в позиции единиц равна ' + d)
n = 12345
print(n // 10000)
print(n % 10000 // 1000)
print(n % 1000 // 100)
print(n % 100 // 10)
print(n % 10)

