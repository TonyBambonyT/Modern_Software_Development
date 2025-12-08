import math

# Практическая работа 7. Вариант 6.

print("--- Задание 1: НОД и НОК ---")
# Задача: Найти НОД и НОК двух чисел, используя функцию алгоритма Евклида.

def get_nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

try:
    num1 = int(input("Введите первое натуральное число: "))
    num2 = int(input("Введите второе натуральное число: "))

    nod = get_nod(num1, num2)

    # НОК: (A*B)//НОД
    nok = (num1 * num2) // nod

    print("НОД:", nod)
    print("НОК:", nok)

except ValueError:
    print("Ошибка: нужно вводить целые числа!")


print("\n--- Задание 2: Площадь четырехугольника ---")
# Задача: Найти площадь четырехугольника по 4 сторонам и диагонали.
# Разбиваем его на два треугольника диагональю.

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

print("Введите стороны четырехугольника и диагональ.")
# Стороны a,b,c,d; диагональ diag образует треугольники (a,b,diag) и (c,d,diag)
a_side = float(input("Сторона a: "))
b_side = float(input("Сторона b: "))
c_side = float(input("Сторона c: "))
d_side = float(input("Сторона d: "))
diag = float(input("Диагональ: "))

s1 = triangle_area(a_side, b_side, diag)
s2 = triangle_area(c_side, d_side, diag)

total_area = s1 + s2

print("Площадь четырехугольника: {:.2f}".format(total_area))