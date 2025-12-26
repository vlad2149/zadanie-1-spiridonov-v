#1
"""def kon_move():
    x1 = int(input("Введите номер столбца первой клетки (1-8): "))
    y1 = int(input("Введите номер строки первой клетки (1-8): "))
    x2 = int(input("Введите номер столбца второй клетки (1-8): "))
    y2 = int(input("Введите номер строки второй клетки (1-8): "))

    if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
        return "Ошибка!"

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        return "Может"
    else:
        return "Не может"


print(kon_move())"""

#2
"""def sum_even_numbers():
    K = int(input("Введите число K: "))
    N = int(input("Введите число N: "))

    total = 0
    for i in range(K, N + 1):
        if i % 2 == 0:
            total += i

    return total


print(f"Сумма четных чисел: {sum_even_numbers()}")"""

#3
"""def sum_until_zero():
    total = 0
    while True:
        num = int(input("Введите число (0 для завершения): "))
        if num == 0:
            break
        total += num

    return total


print(f"Сумма введенных чисел: {sum_until_zero()}")"""

#4
"""def factorial():
    N = int(input("Введите число N: "))

    if N < 0:
        return "Факториал отрицательного числа не определен"

    result = 1
    for i in range(1, N + 1):
        result *= i

    return result


print(f"Факториал числа: {factorial()}")"""