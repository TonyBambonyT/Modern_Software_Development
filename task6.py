def count_factorial(n):
    # Проверяем, что число неотрицательно
    if n < 0:
        return "Ошибка: введите натуральное (положительное) число"

    # Базовый случай: факториал 0 и 1 равен 1
    elif n == 0 or n == 1:
        return 1

    else:
        result = 1

        # Цикл от 2 до n (1 пропускаем)
        for i in range(2, n + 1):
            result = result * i

        return result


# Ввод числа
print("Введите натуральное число n:")
number = int(input())

# Вызываем нашу функцию
fact = count_factorial(number)

# Выводим итог на экран
print("Факториал числа", number, "равен:", fact)