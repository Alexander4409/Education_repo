# def summ(num_1,num_2):
#     print(num_1+num_2)
#
# summ(1,2)


# Простая функция для проверки четности числа
# Функция принимает число и проверяет, является ли оно четным.


# def is_even(number):
#     res = number % 2 == 0
#     return res
#
# print(is_even(4))
# print(is_even(5))


#Сложить все числа переданные в функцию

# def summ(*params):
#     res = 0
#     for num in params:
#         res += num
#     return res
#
# print(summ(1,2,3,4,23,4,1,3,43,21,13,))

#функция для нахождения факториала при помощи цикла

# def fact(n):
#     factorial = 1
#     for _ in range(2,n+1):
#         factorial *= _
#     return factorial
#
# n = int(input("Enter the number"))
# print(fact(n))


#рекурсивный алгоритм
#нахождения факториала
# def facrolial_rec(num):
#     if num == 0:
#         return 1
#     else:
#         return num * facrolial_rec(num-1)
#
# num = int(input())
# print(facrolial_rec(num))

#использование библиотеки math
#
# import math
# print(math.factorial(100))


#Вычисление расстояния между двумя точками
# import math
#
# def distance(x1, y1, x2,y2):
#     return math.sqrt((x2-x1)**2 +(y2 - y1)**2)
#
# print(distance(0,0,3,5))
# import math
# print(math.sqrt(2))
#
# #Функция принимает коэффициенты квадратного уравнения ax^2 + bx + c = 0 и возвращает корни.
# import math
#
# def solve_quadratic(a,b,c):
#     discriminamt = b**2 - 4*a*c
#     if discriminamt > 0:
#         root1 = (-b + math.sqrt(discriminamt)) / (2*a)
#         root2 = (-b - math.sqrt(discriminamt)) / (2*a)
#         return root1, root2
#     elif discriminamt == 0:
#         root = -b/(2*a)
#         return root
#     else:
#         return "No roots"
#
# print(solve_quadratic(1,-3,2))
# print(solve_quadratic(1,-4,7))
# print(solve_quadratic(1,2,1))
# print(solve_quadratic(2,2,2))

#округление
# import math
#
# print(math.ceil(4.2))#округление вверх
# print(math.ceil(4.8))#округление вниз


# def value(cash, usd):
#         try:
#             res = cash/usd
#             if res <= 0:
#                 return "Отрицательный результат"
#             return res
#         except ZeroDivisionError:
#             return 'деление на ноль'
#         except ValueError:
#             return "ошибка ввода"
#
#
# try:
#     cash = int(input())
#     usd = int(input())
#
#     print(f'результат {value(cash,usd)}')
#
# except ValueError:
#     print("Ошибка, введите число")




# try:
#     def celsius_to_fahrenheit_kelvin(celsius):
#
#         fahrenheit = (9 / 5 * celsius) + 32
#         kelvin = celsius + 273.15
#         return fahrenheit, kelvin
# except:
#     print('Температура должна быть числом')




#
# import sympy
#
# from sympy import symbols, expand
#
#
#
# from sympy import symbols, Eq, solve
#
# # Определяем символ x
# x = symbols('x')
#
# # Создаем уравнение
# equation = Eq(x**2 - 4, 0)
#
# # Решаем уравнение
# solutions = solve(equation, x)
# print(solutions)  # Результат: [-2, 2]
from sympy import solve, symbols

# Определяем символ
x = symbols('x')

# Записываем неравенство
inequality = x**2 - 5*x + 6 > 0

# Решаем неравенство
solution = solve(inequality, x)
print(solution)  # Результат: (-∞ < x < 2) ∪ (3 < x < ∞)
