#1
"""def task_27686():
    with open('27686.txt', 'r', encoding='utf-8') as f:
        content = f.read().strip()

    max_length = 0
    current_length = 0

    for char in content:
        if char == 'X':
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 0

    return max_length


result = task_27686()
print(f"Длина самой длинной последовательности X: {result}")"""

#2
"""def task_36037():
    with open('36037.txt', 'r', encoding='utf-8') as f:
        content = f.read().strip()

    max_length = 0
    current_length = 0

    for i in range(len(content)):
        current_length += 1
        if i >= 3:
            if content[i - 3:i + 1] == 'XZZY':
                max_length = max(max_length, current_length - 1)
                current_length = 3

    max_length = max(max_length, current_length)

    return max_length

result = task_36037()
print(f"Максимальная длина без XZZY: {result}")"""

#3
"""def task_46982():
    with open('46982.txt', 'r', encoding='utf-8') as f:
        content = f.read().strip()

    count = 0
    n = len(content)

    for i in range(n):
        if content[i] == 'E':
            for j in range(i + 11, n):  # Минимум 12 символов, значит j ≥ i+11
                if content[j] == 'E':
                    if j - i + 1 >= 12:
                        valid = True

                        for k in range(i + 1, j):
                            if content[k] == 'F':
                                valid = False
                                break
                            if content[k] == 'E':
                                valid = False
                                break

                        if valid:
                            count += 1
                    break

    return count
result = task_46982()
print(f"Количество групп: {result}")"""