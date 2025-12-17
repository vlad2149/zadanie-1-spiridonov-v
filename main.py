#1
"""x1 = int(input("столбца 1-8: "))
y1 = int(input("строки 1-8: "))
x2 = int(input("столбца 1-8: "))
y2 = int(input("строки 1-8: "))

if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
    print("ошибка")
else:
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        print("да, конь может попасть с первой клетки на вторую одним ходом")
    else:
        print("нет, конь не может попасть с первой клетки на вторую одним ходом")"""
        
#2
"""K = int(input("число K: "))
N = int(input("число N: "))

start = min(K, N)
end = max(K, N)

sum_even = 0

for num in range(start, end + 1):
    if num % 2 == 0: 
        sum_even += num

print(f"cумма чётных чисел от K до N включительно: {sum_even}")"""

#3
"""total_sum = 0

while True:
    num = int(input("введите число (0 для завершения): "))
    
    if num == 0:
        break
    
    total_sum += num

print(f"сумма введённых чисел: {total_sum}")"""

#4
"""N = int(input("введите число N: "))

if N < 0:
    print("факториал отрицательного числа не найден")
else:
    factorial = 1
    
    for i in range(1, N + 1):
        factorial *= I
    
    print(f"Факториал числа {N} равен {factorial}")"""