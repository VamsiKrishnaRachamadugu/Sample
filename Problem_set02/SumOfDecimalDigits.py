string = raw_input('Enter the list of numbers')
def sumDigits(s):
    list2 = []
    sum = 0
    for i in string:
        if i.isdigit():
            list2.append(i)
            sum += int(i)
    print list2
    print sum

try:
    sumDigits(string)
except:
    print 'Error'