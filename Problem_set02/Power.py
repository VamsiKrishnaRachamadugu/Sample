class Power:
    def is_power(self, num1, num2):
        quot = num1 / num2
        if quot != num2:
            if num1 % num2 == 0 and quot % num2 == 0:
                return 'true'
            else:
                return 'false'


p = Power()
print p.is_power(32, 2)
