import sys

# Практическая работа 12. Вариант 6.
# Тема: Рекурсия.

sys.setrecursionlimit(2000)

print("--- Блок А. Задача 6 (Проверка на простоту) ---")


# Условие: Проверить, является ли число n простым.

def check_prime(n, divisor):
    # Базовый случай: делитель > sqrt(n) -> n простое
    if divisor * divisor > n:
        return True

    if n % divisor == 0:
        return False

    return check_prime(n, divisor + 1)


try:
    n_input = int(input("Введите натуральное число n > 1: "))

    if n_input <= 1:
        print("Нужно ввести число больше 1.")
    else:
        if check_prime(n_input, 2):
            print("YES")
        else:
            print("NO")

except ValueError:
    print("Ошибка ввода. Введите число.")

print("\n--- Блок Б. Задача 2 (Второй максимум) ---")


# Условие: Найти второй по величине элемент в последовательности, заканчивающейся 0.

def find_second_max():
    num = int(input())

    # 0 - вернуть кортеж из двух нулевых максимумов
    if num == 0:
        return 0, 0

    # Шаг рекурсии: уходим до 0 и берем максимумы из хвоста
    max1, max2 = find_second_max()

    # На обратном пути рекурсии сравниваем num с максимумами хвоста

    if num > max1:
        # Если num > max1, сдвигаем max1 в max2, а num делаем новым max1
        max2 = max1
        max1 = num
    elif num > max2:
        # Если num между max1 и max2, обновляем max2
        max2 = num

    return max1, max2


print("Введите последовательность чисел (каждое с новой строки).")
print("Для завершения введите 0.")

result_m1, result_m2 = find_second_max()

print("Второй по величине элемент:", result_m2)