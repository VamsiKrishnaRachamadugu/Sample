def findAnEven(l):
    for i in l:
        if i % 2 == 0:
            return i
            break
    else:
        raise ValueError


li = [1, 2, 3, 1, 2, 4, 23, 124, 3, 123, 12]
try:
    print  findAnEven(li)
except ValueError as ve:
    print ve.message
