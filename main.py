# ЗАВДАННЯ 1

# Вивести на екран усі прості числа в діапазоні, зазначеному користувачем.
# Число називається простим, якщо воно ділиться без залишку тільки на себе та на одиницю.
# Наприклад, три — це просте число, а чотири — ні.


# start = int(input("Введіть початкове число діапазону: "))
# end = int(input("Введіть кінцеве число діапазону: "))
#
# for number in range(start, end + 1):
#
#     if number / number == 1 and number % 2:   # створюємо умову для простого числа
#         print(number, "- просте число")       # якщо умова виконується це є просте число


# # ЗАВДАННЯ 2
#
#  #Вивести на екран таблицю множення для всіх чисел від 1 до 10.
#
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# for x in range(1, 11):            # 1-ий множник
#     for y in range(1, 11):        # 2-ий множник
#         result = x * y
#         print(f"{x} x {y} = {result}")


# # ЗАВДАННЯ 3
#
# # Вивести на екран таблицю множення в діапазоні, зазначеному користувачем.
#
# numOne = int(input("Введіть початкове число : "))
# numTwo = int(input("Введіть кінцеве число : "))
#
# for x in range(numOne, numTwo + 1):        # створюємо цикл для 1-го множника
#     for y in range(1, 11):                 # створюємо цикл для 2-го множника
#         result = x * y
#         print(f"{x} x {y} = {result}")
