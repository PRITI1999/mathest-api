import random

#Multiplication instead of addition
class AdditionCategory1:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 1
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def generate_answer(cls):
        for i in range(0, len(cls.instance_no_list)):
            cls.answer_calculated = cls.answer_calculated * cls.instance_no_list[i]
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        for i in range(0, no_of_numbers):
            question_generated.append(random.randint(1, 9))
        return question_generated

    def display_message(cls):
        return "comment_a1"

"""list1 = [1, 2, 3]
ac1 = AdditionCategory1(list1)
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))"""

#Missing out a carry at any place
class AdditionCategory2:
    
    instance_no_list = []
    answer_calculated_list = []
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated_list = []
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def is_category_condition_satisfied(cls):
        temp_list = list(cls.instance_no_list)
        while(all(v != 0 for v in temp_list)):
            sum_of_digits = 0
            for i in range(0, len(temp_list)):
                sum_of_digits = sum_of_digits + (temp_list[i] % 10)
                temp_list[i] = temp_list[i] // 10
            if(sum_of_digits > 9):
                return True
        return False
    
    def generate_answer_utility(cls, carry, temp_list, answer_string):
        if(all(v == 0 for v in temp_list)):
            if(carry > 0):
                answer_string = str(carry) + answer_string
            cls.answer_calculated_list.append(int(answer_string))
            answer_string = ''
            return
        sum_of_digits = carry
        for i in range(0, len(temp_list)):
            sum_of_digits = sum_of_digits + (temp_list[i] % 10)
            temp_list[i] = temp_list[i] // 10
        answer_string = str(sum_of_digits % 10) + answer_string
        temp_list_copy = list(temp_list)
        if(sum_of_digits > 9):
            cls.generate_answer_utility(sum_of_digits // 10, temp_list, answer_string)
        cls.generate_answer_utility(0, temp_list_copy, answer_string)
    
    def generate_answer(cls):
        cls.answer_calculated_list = []
        temp_list = list(cls.instance_no_list)
        cls.generate_answer_utility(0, temp_list, '')
        return cls.answer_calculated_list
    
    def generate_question(cls, no_of_numbers):
        
        question_generated = []
        no_of_digits = random.randint(1, 3)
        
        if(no_of_digits == 1):
            num1 = random.randint(5, 9)
            num2 = random.randint(5, 9)
        elif(no_of_digits == 2):
            digit_randomized = random.randint(1, 3)
            if(digit_randomized == 1):
                num1 = random.randint(5, 9) + random.randint(1, 9) * 10;
                num2 = random.randint(5, 9) + random.randint(1, 9) * 10;
            else:
                num1 = random.randint(1, 9) + random.randint(5, 9) * 10;
                num2 = random.randint(1, 9) + random.randint(5, 9) * 10;
        else:
            digit_randomized = random.randint(1, 4)
            if(digit_randomized == 1):
                num1 = random.randint(5, 9) + random.randint(1, 9) * 10 + random.randint(1, 9) * 100;
                num2 = random.randint(5, 9) + random.randint(1, 9) * 10 + random.randint(1, 9) * 100;
            elif(digit_randomized == 2):
                num1 = random.randint(1, 9) + random.randint(5, 9) * 10 + random.randint(1, 9) * 100;
                num2 = random.randint(1, 9) + random.randint(5, 9) * 10 + random.randint(1, 9) * 100;
            else:
                num1 = random.randint(1, 9) + random.randint(1, 9) * 10 + random.randint(5, 9) * 100;
                num2 = random.randint(1, 9) + random.randint(1, 9) * 10 + random.randint(5, 9) * 100;
        
        question_generated.append(num1)
        question_generated.append(num2)
        
        if(no_of_numbers > 2):
            number_left_to_generate = no_of_numbers - 2 
            for i in range(0, number_left_to_generate):
                question_generated.append(random.randint(1, 999))      
        return random.sample(question_generated, len(question_generated))
    
    def display_message(cls):
        return "comment_a2"

"""list1 = [99, 99, 99]
ac1 = AdditionCategory2(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))"""

#Confusion in 6 and 9
class AdditionCategory3:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def is_category_condition_satisfied(cls):
        for i in range(len(cls.instance_no_list)):
            s = set(str(cls.instance_no_list[i]))
            if('6' in s or '9' in s):
                return True
        return False
    
    def generate_answer(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(0, len(temp_list)):
            num =  str(temp_list[i])
            for i in range(len(num)):
                if(num[i] == '6'):
                    num  = num[:i] + '9' + num[i+1:]
                elif(num[i] == '9'):
                    num  = num[:i] + '6' + num[i+1:]
            cls.answer_calculated = cls.answer_calculated + int(num)
        cls.answer_calculated = str(cls.answer_calculated)
        for i in range(len(cls.answer_calculated)):
            if(cls.answer_calculated[i] == '6'):
                cls.answer_calculated = cls.answer_calculated[:i] + '9' + cls.answer_calculated[i+1:]
            elif(cls.answer_calculated[i] == '9'):
                cls.answer_calculated  = cls.answer_calculated[:i] + '6' + cls.answer_calculated[i+1:]
        cls.answer_calculated = int(cls.answer_calculated)
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        no_of_digits = random.randint(1, 3)
        if(no_of_digits == 1):
            num1 = 6
            num2 = 9
        elif(no_of_digits == 2):
            num1 = 60 + random.randint(1, 9)
            num2 = 90 + random.randint(1, 9)
        else:
            num1 = 600 + random.randint(1, 99)
            num2 = 900 + random.randint(1, 99)
        
        question_generated.append(num1)
        question_generated.append(num2)
        
        if(no_of_numbers > 2):
            number_left_to_generate = no_of_numbers - 2 
            for i in range(0, number_left_to_generate):
                question_generated.append(random.randint(1, 999))
        return random.sample(question_generated, len(question_generated))
    
    def display_message(cls):
        return "comment_a3"

"""list1 = [16, 45, 5]
ac1 = AdditionCategory3(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))"""

#Confusion in 1 and 7
class AdditionCategory4:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0;
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def is_category_condition_satisfied(cls):
        for i in range(len(cls.instance_no_list)):
            s = set(str(cls.instance_no_list[i]))
            if('1' in s or '7' in s):
                return True
        return False
    
    def generate_answer(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(0, len(temp_list)):
            num =  str(temp_list[i])
            for i in range(len(num)):
                if(num[i] == '1'):
                    num  = num[:i] + '7' + num[i+1:]
                elif(num[i] == '7'):
                    num  = num[:i] + '1' + num[i+1:]
            cls.answer_calculated = cls.answer_calculated + int(num)

        cls.answer_calculated = str(cls.answer_calculated)
        for i in range(len(cls.answer_calculated)):
            if(cls.answer_calculated[i] == '1'):
                cls.answer_calculated = cls.answer_calculated[:i] + '7' + cls.answer_calculated[i+1:]
            elif(cls.answer_calculated[i] == '7'):
                cls.answer_calculated  = cls.answer_calculated[:i] + '1' + cls.answer_calculated[i+1:]
        cls.answer_calculated = int(cls.answer_calculated)
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        no_of_digits = random.randint(1, 3)
        if(no_of_digits == 1):
            num1 = 1
            num2 = 7
        elif(no_of_digits == 2):
            num1 = 10 + random.randint(1, 9)
            num2 = 70 + random.randint(1, 9)
        else:
            num1 = 100 + random.randint(1, 99)
            num2 = 700 + random.randint(1, 99)
        
        question_generated.append(num1)
        question_generated.append(num2)
        
        if(no_of_numbers > 2):
            number_left_to_generate = no_of_numbers - 2 
            for i in range(0, number_left_to_generate):
                question_generated.append(random.randint(1, 999))
        return random.sample(question_generated, len(question_generated))
    
    def display_message(cls):
        return "comment_a4"

"""list1 = [17, 45, 5]
ac1 = AdditionCategory4(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))"""

#Confusion in 1, 7 and 6, 9
class AdditionCategory5:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def is_category_condition_satisfied(cls):
        for i in range(len(cls.instance_no_list)):
            s = set(str(cls.instance_no_list[i]))
            if('6' in s or '9' in s and '1' in s or '7' in s):
                return True
        return False
    
    def generate_answer(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(0, len(temp_list)):
            num =  str(temp_list[i])
            for i in range(len(num)):
                if(num[i] == '6'):
                    num  = num[:i] + '9' + num[i+1:]
                elif(num[i] == '9'):
                    num  = num[:i] + '6' + num[i+1:]
                elif(num[i] == '1'):
                    num  = num[:i] + '7' + num[i+1:]
                elif(num[i] == '7'):
                    num  = num[:i] + '1' + num[i+1:]
            cls.answer_calculated = cls.answer_calculated + int(num)
        cls.answer_calculated = str(cls.answer_calculated)
        for i in range(len(cls.answer_calculated)):
            if(cls.answer_calculated[i] == '6'):
                cls.answer_calculated = cls.answer_calculated[:i] + '9' + cls.answer_calculated[i+1:]
            elif(cls.answer_calculated[i] == '9'):
                cls.answer_calculated  = cls.answer_calculated[:i] + '6' + cls.answer_calculated[i+1:]
            elif(cls.answer_calculated[i] == '1'):
                cls.answer_calculated = cls.answer_calculated[:i] + '7' + cls.answer_calculated[i+1:]
            elif(cls.answer_calculated[i] == '7'):
                cls.answer_calculated  = cls.answer_calculated[:i] + '1' + cls.answer_calculated[i+1:]
        cls.answer_calculated = int(cls.answer_calculated)
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        no_of_digits = random.randint(1, 3)
        pair = random.randint(1,2)
        if(no_of_digits == 1 and pair == 1):
            num1 = 6 
            num2 = 7
        elif(no_of_digits == 1 and pair == 2):
            num1 = 1
            num2 = 9
        elif(no_of_digits == 2 and pair == 1):
            num1 = 60 + random.randint(1, 9)
            num2 = 70 + random.randint(1, 9)       
        elif(no_of_digits == 2 and pair == 2):
            num1 = 10 + random.randint(1, 9)
            num2 = 90 + random.randint(1, 9)
        elif(pair == 1):
            num1 = 600 + random.randint(1, 99)
            num2 = 700 + random.randint(1, 99)
        else:
            num1 = 100 + random.randint(1, 99)
            num2 = 900 + random.randint(1, 99)
        question_generated.append(num1)
        question_generated.append(num2)
        
        if(no_of_numbers > 2):
            number_left_to_generate = no_of_numbers - 2 
            for i in range(0, number_left_to_generate):
                question_generated.append(random.randint(1, 999))
        return random.sample(question_generated, len(question_generated))
    
    def display_message(cls):
        return "comment_a5"

"""list1 = [16, 45, 5]
ac1 = AdditionCategory5(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))"""

#Left to right addition
class AdditionCategory6:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def is_category_condition_satisfied(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(0, len(temp_list)):
            temp_list[i] = temp_list[i] // 10
        if(all(v != 0 for v in temp_list)):
            return True
        return False
    
    def generate_answer(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(0, len(temp_list)):
            temp_list[i] = str(temp_list[i])
            temp_list[i] = temp_list[i][::-1]
            cls.answer_calculated = cls.answer_calculated + int(temp_list[i])
        cls.answer_calculated = str(cls.answer_calculated)
        cls.answer_calculated = cls.answer_calculated[::-1]
        return int(cls.answer_calculated)
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        for i in range(0, no_of_numbers):
            question_generated.append(100 * random.randint(1, 9) + 10 * random.randint(1,9) + random.randint(1,9))
        return question_generated

    def display_message(cls):
        return "comment_a6"

"""list1 = [123, 72]
ac1 = AdditionCategory6(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))"""

#Ignoring 0 at the end
class AdditionCategory7:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
        
    def is_category_condition_satisfied(cls):
        for i in range(len(cls.instance_no_list)):
            if(cls.instance_no_list[i] % 10 == 0):
                return True
        return False
    
    def generate_answer(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(len(temp_list)):
            while(temp_list[i] % 10 == 0):
                temp_list[i] = temp_list[i] // 10
            cls.answer_calculated = cls.answer_calculated + temp_list[i]
            while(cls.answer_calculated % 10 == 0):
                cls.answer_calculated = cls.answer_calculated // 10
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        num1 = random.randint(1,9) * 10
        num2 = random.randint(10,99) * 10
        question_generated.append(num1)
        question_generated.append(num2)
        if(no_of_numbers > 2):
            number_left_to_generate = no_of_numbers - 2 
            for i in range(0, number_left_to_generate):
                question_generated.append(random.randint(1, 999))
        return random.sample(question_generated, len(question_generated))

    def display_message(cls):
        return "comment_a7"

"""list1 = [1010, 601, 301]
ac1 = AdditionCategory7(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))"""

#Ignoring 0 in the middle
class AdditionCategory8:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
        
    def is_category_condition_satisfied(cls):
        for i in range(len(cls.instance_no_list)):
            if('0' in str(cls.instance_no_list[i])[1:-1]):
                return True
        return False
    
    def generate_answer(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(len(temp_list)):
            while(temp_list[i] % 10 == 0):
                temp_list[i] = temp_list[i] // 10
            cls.answer_calculated = cls.answer_calculated + temp_list[i]
            while(cls.answer_calculated % 10 == 0):
                cls.answer_calculated = cls.answer_calculated // 10
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        num1 = int(str(random.randint(1,9)) + '0' + str(random.randint(1,9)))
        num2 = int(str(random.randint(1,9)) + '0' + str(random.randint(1,9)))
        question_generated.append(num1)
        question_generated.append(num2)
        if(no_of_numbers > 2):
            number_left_to_generate = no_of_numbers - 2 
            for i in range(0, number_left_to_generate):
                question_generated.append(random.randint(1,9) * 100 + random.randint(0,9) * 10 + random.randint(1,9))
        return random.sample(question_generated, len(question_generated))
    
    def display_message(cls):
        return "comment_a8"

"""list1 = [101, 601, 301]
ac1 = AdditionCategory8(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))"""
