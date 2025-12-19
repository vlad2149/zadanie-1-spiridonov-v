#1
"""N = int(input())

if N <= 0:
    print(0)
elif N == 1:
    print(1)
else:
    a, b = 0, 1
    for _ in range(0, N + 1):
        a, b = b, a + b
    print(b)"""
    
    #2
"""n = int(input())
mas = [0] * (n + 1)
mas[0], mas[1] = 1, 1
for i in range(2, n + 1):
    mas[i] = mas[i - 1] + (mas[i - 2] if i - 2 >= 0 else 0) + (mas[i - 3] if i - 3 >= 0 else 0)
    
print(mas[n])"""

#3
"""coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0, 0, 0, 1],
]
n = 4
m = 6

dp = [row[:] for row in coins]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            dp[i][j] = dp[i][j-1] + coins[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + coins[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + coins[i][j]


path = []
i, j = n-1, m-1
while i > 0 or j > 0:
    path.append((i, j))
    if i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1
path.append((0, 0))
path.reverse()

print("Максимальное количество монет:", dp[-1][-1])
print("Путь (координаты):", path)


dirs = []
for k in range(1, len(path)):
    pi, pj = path[k-1]
    ci, cj = path[k]
    if ci == pi + 1:
        dirs.append("вниз")
    else:
        dirs.append("вправо")

print("Направления:", " → ".join(dirs))


total = 0
for (i, j) in path:
    total += coins[i][j]
print("Монет собрано:", total)"""