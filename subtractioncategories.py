import random

#Addition instead of subtraction
class SubtractionCategory1:
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def generate_answer(cls):
        for i in range(0, len(cls.instance_no_list)):
            cls.answer_calculated = cls.answer_calculated + cls.instance_no_list[i]
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        num1 = random.randint(10, 99)
        num2 = random.randint(1, 9)
        question_generated.append(num1)
        question_generated.append(num2)
        return question_generated
    
    def display_message(cls):
        return "comment_s1" 

"""list1 = [45, 7, 5]
sc1 = SubtractionCategory1(list1)
print(sc1.generate_answer())
print(sc1.generate_question())"""

#Division instead of subtraction
class SubtractionCategory2:
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def generate_answer(cls):
        cls.answer_calculated = cls.instance_no_list[0] / cls.instance_no_list[1]
        #for i in range(0, len(cls.instance_no_list)):
            # cls.answer_calculated = cls.answer_calculated[0] / cls.instance_no_list[1]
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        num1 = random.randint(1, 999)
        num2 = random.randint(1, 999)
        while(num2>num1):
            num2 = random.randint(1,999)   
        question_generated.append(num1)
        question_generated.append(num2)
        return question_generated
    
    def display_message(cls):
        return "comment_s2"

"""list2 = [415, 7]
sc2 = SubtractionCategory2(list2)
print(sc2.generate_answer())
print(sc2.generate_question(len(list2)))"""

#First num > Second num as negative subtraction not being handled.
#After carrying over a 1, forgetting to subtract it from the number that gave the carry.

class SubtractionCategory3:
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])

    def is_category_condition_satisfied(cls):
        temp_list = list(cls.instance_no_list)
        #print(temp_list[0])
        #print(temp_list[1])
        num_1_list =[]
        num_2_list =[]
        while (temp_list[0]>0):
           num_1_list.append(temp_list[0] % 10)
           temp_list[0] = temp_list[0] // 10
        while (temp_list[1]>0):
           num_2_list.append(temp_list[1] % 10)
           temp_list[1] = temp_list[1] // 10
        #print(num_1_list)
        #print(num_2_list)
        for i in range(0,len(num_1_list)):
            if (i>=len(num_2_list)):
                break;
            if(num_1_list[i]<num_2_list[i]):
                return True
        return False
    
    def generate_answer_utility(cls, temp_list, answer_string):
        temp_list = list(cls.instance_no_list)
        num_1_list =[]
        num_2_list =[]
        while (temp_list[0]>0):
           num_1_list.append(temp_list[0] % 10)
           temp_list[0] = temp_list[0] // 10
        while (temp_list[1]>0):
           num_2_list.append(temp_list[1] % 10)
           temp_list[1] = temp_list[1] // 10
        for i in range(0,len(num_1_list)):
            if (i>=len(num_2_list)):
                answer_string = answer_string+str(num_1_list[i])
                continue
            if(num_1_list[i]<num_2_list[i]):
                num_1_list[i]+=10
                answer_string = answer_string+str(num_1_list[i]-num_2_list[i])
                #num_1_list[i+1]-=1
            else:
                answer_string = answer_string+str(num_1_list[i]-num_2_list[i])
        cls.answer_calculated_list.append(int(answer_string[::-1]))
        return

    def generate_answer(cls):
        cls.answer_calculated_list = []
        temp_list = list(cls.instance_no_list)
        cls.generate_answer_utility(temp_list, '')
        return cls.answer_calculated_list
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        num1 = random.randint(1, 999)
        num2 = random.randint(1, 999)
        sub3 = SubtractionCategory3([num1,num2])
        while(not(sub3.is_category_condition_satisfied()) and num2>num1 ):
            num2 = random.randint(1,999)
            sub3 = SubtractionCategory3([num1,num2])
        question_generated.append(num1 if num1>num2 else num2)
        question_generated.append(num2 if num2<num1 else num1)
        return question_generated
    
    def display_message(cls):
        return "comment_s3"

"""list3 = [744, 69]
sc3 = SubtractionCategory3(list3)
print(sc3.is_category_condition_satisfied())
print(sc3.generate_answer())
print(sc3.generate_question(len(list3)))"""
