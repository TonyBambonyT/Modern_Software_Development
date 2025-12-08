# Практическая работа 4. Задача 7. (т.к. 6 задачу делал в разделе контрольная работа: https://github.com/TonyBambonyT/Modern_Software_Development/blob/main/task6.py)
# Вычислить сумму факториалов 1! + 2! + ... + n!
# Условие: использовать только один цикл, без math.

n = int(input("Введите натуральное число n: "))

current_factorial = 1
total_sum = 0

for i in range(1, n + 1):
    # Факториал: на каждом шаге умножаем предыдущее значение на i
    current_factorial = current_factorial * i

    total_sum = total_sum + current_factorial

print("Сумма факториалов от 1! до", n, "! равна:", total_sum)
