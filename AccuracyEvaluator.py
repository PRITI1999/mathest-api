#import random
from decimal import Decimal
# Inputs:
#   - the correct ans , indexed by 0
#   - user's answer, indexed by 1
position_list = ['Units','Tens','Hundreds','Thousands','Ten Thousands']
class Accuracy:
    
    instance_no_list = []
    #accuracy_correct=0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        #self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def get_accuracy(cls):
        
        temp_list = list(cls.instance_no_list)
        user_ans_list = []
        correct_ans_list =[]
        correct_ans = temp_list[0]
        accuracy_matrix =[]

        while (correct_ans>0):
           correct_ans_list.append(correct_ans % 10)
           correct_ans = correct_ans // 10
        while (temp_list[1]>0):
           user_ans_list.append(temp_list[1] % 10)
           temp_list[1] = temp_list[1] // 10   
        
        for i in range(0,len(correct_ans_list)):
            if(i<len(user_ans_list)):
                if(user_ans_list[i]==correct_ans_list[i]):
                    accuracy_matrix.append(1)
                    continue
            accuracy_matrix.append(0)
        
        # accuracy_matrix is stored in the order the numbers appear, this has to be reversed to print the 
        min_flag=1
        s = float(sum(accuracy_matrix))
        l = int(len(accuracy_matrix))
        accuracy = Decimal(s/l)
        for i in range(0,len(accuracy_matrix)):
            if(min_flag==1 and accuracy_matrix[i]==0):
                print("Your "+position_list[i]+" is wrong")
                min_flag=0
        
        print("Your answer is "+str(round(accuracy,2))+"% right")

        return round(accuracy,2)
    

list1 = [2, 12]
ac =Accuracy(list1)
print(ac.get_accuracy())