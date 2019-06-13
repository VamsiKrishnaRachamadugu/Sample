def non_recursive(n):
    fact = 1
    if n == 0:
        return 1
    for i in range(1, n+1):
        fact *= i
    return fact


def recursive(n):
    if n == 0:
        return 1
    else:
        return n * recursive(n - 1)


num = 5
print non_recursive(num)
print  recursive(num)
