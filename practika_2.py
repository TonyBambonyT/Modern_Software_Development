import math

# Практическая работа 2. Вариант 6.

# Исходные данные
x = 16.55 * 10**-3
y = -2.75
z = 0.15

# 1. Вычисляем подкоренное
term1 = x**(1/3)
term2 = x**(y + 2)
under_root = 10 * (term1 + term2)
part1 = math.sqrt(under_root)

# 2. Считаем правую часть
asin_squared = math.asin(z)**2
abs_diff = math.fabs(x - y)

part2 = asin_squared - abs_diff

# 3. Итоговый результат - перемножаем части
s = part1 * part2

# Выводим результат
print("x =", x)
print("y =", y)
print("z =", z)

# Форматируем вывод, чтобы было похоже на ответ в задании (там 4 знака)
print("Результат s = {:.4f}".format(s))