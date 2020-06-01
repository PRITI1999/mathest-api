import array

def numberOfDigits(number):
    if number == 0:
        return 1
    count = 0
    while number != 0:
        count = count + 1
        number = number // 10
    return count

def multiplication_working(uid, number1, number2):
    
    number1 = int(number1)
    number2 = int(number2)
    number1copy = number1
    number2copy = number2
    carry = array.array('i', [0, 0, 0, 0, 0, 0])
    number1array = array.array('i', [-1, -1, -1])
    number2array = array.array('i', [-1, -1, -1])
    subnum1array = array.array('i', [-1, -1, -1, -1, -1, -1])
    subnum2array = array.array('i', [-1, -1, -1, -1, -1, -1])
    subnum3array = array.array('i', [-1, -1, -1, -1, -1, -1])
    resultarray = array.array('i', [-1, -1, -1, -1, -1, -1])
    
    i = 0
    if number1copy == 0:
        number1array[0] = 0
    while number1copy != 0:
        number1array[i] = number1copy % 10
        number1copy = number1copy // 10
        i = i + 1
    
    i = 0
    if number2copy == 0:
        number2array[0] = 0
    while number2copy != 0:
        number2array[i] = number2copy % 10
        number2copy = number2copy // 10
        i = i + 1
    
    if number2array[0] != -1:
        product = number2array[0] * number1
        i = 0
        if product == 0:
            j = 0
            while j < numberOfDigits(number1):
                subnum1array[j] = 0
                j = j + 1
        while product != 0:
            subnum1array[i] = product % 10
            product = product // 10
            i = i + 1    
    
    if number2array[1] != -1:
        product = number2array[1] * number1
        i = 1
        if product == 0:
            j = 1
            while j < numberOfDigits(number1) + 1:
                subnum2array[j] = 0
                j = j + 1
        while product != 0:
            subnum2array[i] = product % 10
            product = product // 10
            i = i + 1 
        
    if number2array[2] != -1:
        product = number2array[2] * number1
        i = 2
        if product == 0:
             j = 2
             while j < numberOfDigits(number1) + 2:
                subnum3array[j] = 0
                j = j + 1
        while product != 0:
            subnum3array[i] = product % 10
            product = product // 10
            i = i + 1
    
    for i in range(5):
        if subnum1array[i] != -1 or subnum2array[i] != -1 or subnum3array[i] != -1:
            sum_of_digits = subnum1array[i] + subnum2array[i] + subnum3array[i] + carry[i]
            if subnum1array[i] == -1:
                sum_of_digits = sum_of_digits + 1
            if subnum2array[i] == -1:
                sum_of_digits = sum_of_digits + 1
            if subnum3array[i] == -1:
                sum_of_digits = sum_of_digits + 1
            if sum_of_digits > 19:
                carry[i + 1] = 2
                sum_of_digits = sum_of_digits % 10
            elif sum_of_digits > 9:
                carry[i + 1] = 1
                sum_of_digits = sum_of_digits % 10
            else:
                carry[i + 1] = 0
            resultarray[i] = sum_of_digits
    
    if carry[5] > 0:
        sum_of_digits = subnum1array[5] + subnum2array[5] + subnum3array[5] + carry[5]
        if subnum1array[5] == -1:
            sum_of_digits = sum_of_digits + 1
        if subnum2array[5] == -1:
            sum_of_digits = sum_of_digits + 1
        if subnum3array[5] == -1:
            sum_of_digits = sum_of_digits + 1
        resultarray[5] = sum_of_digits
        
    carry.reverse()
    number1array.reverse()
    number2array.reverse()
    subnum1array.reverse()
    subnum2array.reverse()
    subnum3array.reverse()
    resultarray.reverse()
    
    workingDict = [
            {
                    'uid': uid,
                    'object1': 'number1',
                    'object2': 'number2',
                    'object3': 'carry',
                    'object4': 'subnum1',
                    'object5': 'subnum2',
                    'object6': 'subnum3',
                    'object7': 'result'
            },
            {
                    'digit1': number1array[0],
                    'digit2': number1array[1],
                    'digit3': number1array[2]
            },
            {
                    'digit1': number2array[0],
                    'digit2': number2array[1],
                    'digit3': number2array[2]
            },
            {
                    'digit1': carry[0],
                    'digit2': carry[1],
                    'digit3': carry[2],
                    'digit4': carry[3],
                    'digit5': carry[4],
                    'digit6': carry[5]
            },
            {
                    'digit1': subnum1array[0],
                    'digit2': subnum1array[1],
                    'digit3': subnum1array[2],
                    'digit4': subnum1array[3],
                    'digit5': subnum1array[4],
                    'digit6': subnum1array[5]
            },
            {
                    'digit1': subnum2array[0],
                    'digit2': subnum2array[1],
                    'digit3': subnum2array[2],
                    'digit4': subnum2array[3],
                    'digit5': subnum2array[4],
                    'digit6': subnum2array[5]
            },
            {
                    'digit1': subnum3array[0],
                    'digit2': subnum3array[1],
                    'digit3': subnum3array[2],
                    'digit4': subnum3array[3],
                    'digit5': subnum3array[4],
                    'digit6': subnum3array[5]
            },
            {
                    'digit1': resultarray[0],
                    'digit2': resultarray[1],
                    'digit3': resultarray[2],
                    'digit4': resultarray[3],
                    'digit5': resultarray[4],
                    'digit6': resultarray[5]
            }
    ]
    
    return workingDict
    
    """print(carry)
    print(number1array)
    print(number2array)
    print(subnum1array)
    print(subnum2array)
    print(subnum3array)
    print(resultarray)"""

"""uid = 123        
number1 = 100
number2 = 100
multiplication_working(uid, number1, number2)"""
