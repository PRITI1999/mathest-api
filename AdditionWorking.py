import array

def addition_working(uid, number1, number2):

    number1copy = int(number1)
    number2copy = int(number2)
    carry = array.array('i', [0, 0, 0, 0])
    number1array = array.array('i', [-1, -1, -1])
    number2array = array.array('i', [-1, -1, -1])
    resultarray = array.array('i', [-1, -1, -1, -1])

    i = 0
    while number1copy != 0:
        number1array[i] = number1copy % 10
        number1copy = number1copy // 10
        i = i + 1
    i = 0
    while number2copy != 0:
        number2array[i] = number2copy % 10
        number2copy = number2copy // 10
        i = i + 1
    
    for i in range(3):
        if number1array[i] != -1 or number2array[i] != -1:
            sum_of_digits = number1array[i] + number2array[i] + carry[i]
            if number1array[i] == -1:
                sum_of_digits = sum_of_digits + 1
            if number2array[i] == -1:
                sum_of_digits = sum_of_digits + 1
            if sum_of_digits > 9:
                carry[i + 1] = 1
                sum_of_digits = sum_of_digits % 10
            else:
                carry[i + 1] = 0
            resultarray[i] = sum_of_digits
    
    if carry[3] == 1:
        resultarray[3] = carry[3]
        
    carry.reverse()
    number1array.reverse()
    number2array.reverse()
    resultarray.reverse()
    
    workingDict = [
             {
                     'uid': uid,
                     'object1': 'carry',
                     'object2': 'number1',
                     'object3': 'number2',
                     'object4': 'result'
             },
             {
                    'digit1': carry[0],
                    'digit2': carry[1],
                    'digit3': carry[2],
                    'digit4': carry[3]
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
                    'digit1': resultarray[0],
                    'digit2': resultarray[1],
                    'digit3': resultarray[2],
                    'digit4': resultarray[3]
            }
    ]
    
    return workingDict
    
    """print(carry)
    print(number1array)
    print(number2array)
    print(resultarray)"""
   
"""uid = 123
number1 = 656
number2 = 6
addition_working(uid, number1, number2)"""