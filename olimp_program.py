#1
"""def long_inc_subs(nums):

    n = len(nums)
    if n == 0:
        return 0

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums = [6, 2, 5, 4, 2, 5, 6]
print(f"Длина наибольшей возрастающей подпоследовательности: {long_inc_subs(nums)}")"""

#2
"""def read_and_solve(filename="input.txt"):

    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        nums = list(map(int, f.readline().strip().split()))

    if n != len(nums):
        print("Внимание: указанная длина не соответствует количеству чисел!")
        n = len(nums)

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:  # строгое возрастание
                dp[i] = max(dp[i], dp[j] + 1)

    result = max(dp) if dp else 0


    print(f"Длина наибольшей возрастающей подпоследовательности: {result}")
    return result"""

#3
"""def reverse_number(n):
    return int(str(n)[::-1])


def count_k_amazing(k):
    count = 0
    amazing_numbers = []

    for x in range(k + 1):
        if x + reverse_number(x) == k:
            count += 1
            amazing_numbers.append(x)

    return count, amazing_numbers


K = 1050
count, numbers = count_k_amazing(K)
print(f"Для K = {K} найдено {count} K-удивительных чисел:")
print(f"Числа: {numbers}")

def count_k_amazing_fast(k):
    count = 0

    for x in range(k + 1):

        rev_x = int(str(x)[::-1])
        if x + rev_x == k:
            count += 1

    return count


print(f"\nБыстрый алгоритм: {count_k_amazing_fast(1050)} чисел")"""