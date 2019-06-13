number = 34
binary = ''
while number != 0:
    binary = str(number % 2)+binary
    number = number / 2
print binary
