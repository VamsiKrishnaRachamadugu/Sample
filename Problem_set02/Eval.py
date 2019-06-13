import math
def eval_loop():
    li = []
    result = 'false'
    while result == 'false':
        string = raw_input('Enter expression')
        if string == 'done':
            print li
            result = 'true'
            break
        else:
            li.append(eval(string))
            continue


eval_loop()
