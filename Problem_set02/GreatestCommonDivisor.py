def greatestCommon(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatestCommon(b, a % b)


num1 = input('Enter 1st value')
num2 = input('Enter 2nd value')
print greatestCommon(num1, num2)
