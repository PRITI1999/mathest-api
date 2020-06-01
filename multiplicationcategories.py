import random

#Missing out 0s at the end in answer
class MultiplicationCategory1:
    
    instance_no_list = []
    answer_calculated_list = []
    product = 1
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated_list = []
        for i in range(len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def is_category_condition_satisfied(cls):
        cls.product = 1
        for i in range(len(cls.instance_no_list)):
            cls.product = cls.product * cls.instance_no_list[i]
        if(cls.product % 10 == 0):
            return True
        else:
            return False
        
    def generate_answer(cls):
        while cls.product % 10 == 0 and cls.product != 0:
            cls.answer_calculated_list.append(cls.product//10)
            cls.product = cls.product // 10
        if cls.product == 0:
            cls.answer_calculated_list.append(0)
        return cls.answer_calculated_list
        
    def generate_question(cls, no_of_numbers):
        question_generated = []
        num = 10 * random.randint(1, 99)
        question_generated.append(num)
        for i in range(no_of_numbers - 1):
            num1 = random.randint(1, 99)
            question_generated.append(num1)
        return question_generated
    
    def display_message(cls):
        return "comment_m1" 

"""list1 = [85, 100]
mc1 = MultiplicationCategory1(list1)
print(mc1.is_category_condition_satisfied())
print(mc1.generate_answer())
print(mc1.generate_question(len(list1)))"""

#Addition instead of multiplication
class MultiplicationCategory2:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def generate_answer(cls):
        for i in range(len(cls.instance_no_list)):
            cls.answer_calculated = cls.answer_calculated + cls.instance_no_list[i]
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        question_generated.append(random.randint(0, 999))
        question_generated.append(random.randint(0, 999))
        return question_generated
    
    def display_message(cls):
        return "comment_m2"
    
"""list2 = [10, 10]
mc2 = MultiplicationCategory2(list2)
print(mc2.generate_answer())
print(mc2.generate_question(len(list2)))"""

#Place value error, do not shift the numbers while adding
class MultiplicationCategory3:
    
    instance_no_list = []
    answer_calculated = []
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = []
        for i in range(len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
            
    def is_category_condition_satisfied(cls):
        for i in range(len(cls.instance_no_list)):
            if(cls.instance_no_list[i] < 10):
                return False
        return True
    
    def generate_answer(cls):
        
        result = 0
        number1 = cls.instance_no_list[0]
        number2 = cls.instance_no_list[1]
        while number2 != 0:
            result = result + (number2 % 10) * (number1)
            number2 = number2 // 10
        cls.answer_calculated.append(result)
        
        result = 0
        number1 = cls.instance_no_list[0]
        number2 = cls.instance_no_list[1]
        while number1 != 0:
            result = result + (number1 % 10) * (number2)
            number1 = number1 // 10
        cls.answer_calculated.append(result)
        
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        for i in range(no_of_numbers):
            question_generated.append(random.randint(10, 999))
        return question_generated
    
    def display_message(cls):
        return "comment_m3"

"""list3 = [12, 13]
mc3 = MultiplicationCategory3(list3)
print(mc3.is_category_condition_satisfied())
print(mc3.generate_answer())
print(mc3.generate_question(len(list3)))"""

#Misunderstood concept of 0
class MultiplicationCategory4:
    
    instance_no_list = []
    answer_calculated = 1
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 1
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
        
    def is_category_condition_satisfied(cls):
        for i in range(len(cls.instance_no_list)):
            if(cls.instance_no_list[i] % 10 == 0):
                return True
            elif('0' in str(cls.instance_no_list[i])[1:-1]):
                return True
        return False
    
    def generate_answer(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(0, len(temp_list)):
            num = str(temp_list[i])
            for j in range(len(num)):
                if(num[j] == '0'):
                    num  = num[:j] + '1' + num[j+1:]
            cls.instance_no_list[i] = int(num)
        for i in range(len(cls.instance_no_list)):
            cls.answer_calculated = cls.answer_calculated * cls.instance_no_list[i]
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        no_of_digits = random.randint(1, 3)
        num1 = 0
        num2 = 0
        if no_of_digits == 1:
            num1 = 0
            num2 = random.randint(0, 9)
        elif no_of_digits == 2:
            num1 = random.randint(1, 9) * 10
            num2 = random.randint(1, 9) * 10
        else:
            digit_randomized = random.randint(1, 3)
            if digit_randomized == 1:
                num1 = random.randint(1, 9) * 100 + random.randint(1, 9)
                num2 = random.randint(1, 9) * 100 + random.randint(1, 9)
            elif digit_randomized == 2:
                num1 = random.randint(1, 9) * 100 + random.randint(1, 9) * 10
                num2 = random.randint(1, 9) * 100 + random.randint(1, 9) * 10
        
        if num1 == 0 and num2 == 0:
            num1 = random.randint(1, 9)

        question_generated.append(num1)
        question_generated.append(num2)
        
        return random.sample(question_generated, len(question_generated))
        
    def display_message(cls):
        return "comment_m4"

"""list4 = [3, 30]
mc4 = MultiplicationCategory4(list4)
print(mc4.is_category_condition_satisfied())
print(mc4.generate_answer())
print(mc4.generate_question(len(list4)))"""
