import random

# Практическая работа 8. Вариант 6.

print("--- Задание 1 ---")
# 1. Дана целочисленная квадратная матрица.
# Найти в каждой строке наибольший элемент, а в каждом столбце наименьший.

n = int(input("Введите размер матрицы N: "))

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(10, 99))  # числа от 10 до 99 для красоты
    matrix.append(row)

print("Сгенерированная матрица:")
for row in matrix:
    for elem in row:
        print("{:4d}".format(elem), end='')
    print()

print("\nРезультаты:")

print("Максимумы в строках: ", end='')
for row in matrix:
    max_in_row = row[0]
    for elem in row:
        if elem > max_in_row:
            max_in_row = elem
    print(max_in_row, end=' ')
print()

print("Минимумы в столбцах: ", end='')
for j in range(n):
    min_in_col = matrix[0][j]
    for i in range(n):
        if matrix[i][j] < min_in_col:
            min_in_col = matrix[i][j]
    print(min_in_col, end=' ')
print("\n")

print("-" * 20)
print("--- Задание 2 ---")
# 2. Дана действительная матрица (N - нечетное).
# Найти макс. элемент на диагоналях (главной и побочной)
# и поменять его местами с центром (пересечением диагоналей).

while True:
    n2 = int(input("Введите размер матрицы N (нечетное число): "))
    if n2 % 2 != 0:
        break
    print("Число должно быть нечетным!")

matrix_2 = []
for i in range(n2):
    row = []
    for j in range(n2):
        val = round(random.randint(10, 90) + random.random(), 2)
        row.append(val)
    matrix_2.append(row)

print("Исходная матрица:")
for row in matrix_2:
    for elem in row:
        print("{:6.2f}".format(elem), end='')
    print()

center_idx = n2 // 2
max_val = matrix_2[center_idx][center_idx]
max_i = center_idx
max_j = center_idx

for i in range(n2):
    if matrix_2[i][i] > max_val:
        max_val = matrix_2[i][i]
        max_i = i
        max_j = i

    side_idx = n2 - 1 - i
    if matrix_2[i][side_idx] > max_val:
        max_val = matrix_2[i][side_idx]
        max_i = i
        max_j = side_idx

print(f"\nМаксимальный элемент на диагоналях: {max_val} (строка {max_i}, столбец {max_j})")
print(f"Центральный элемент: {matrix_2[center_idx][center_idx]}")

# Меняем максимум с центром через множественное присваивание
matrix_2[center_idx][center_idx], matrix_2[max_i][max_j] = matrix_2[max_i][max_j], matrix_2[center_idx][center_idx]

print("\nМатрица после замены:")
for row in matrix_2:
    for elem in row:
        print("{:6.2f}".format(elem), end='')
    print()