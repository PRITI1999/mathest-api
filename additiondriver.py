import gspread
#import pprint
from oauth2client.service_account import ServiceAccountCredentials
import random
from additioncategories import AdditionCategory1
from additioncategories import AdditionCategory2
from additioncategories import AdditionCategory3
from additioncategories import AdditionCategory4
from additioncategories import AdditionCategory5
from additioncategories import AdditionCategory6
from additioncategories import AdditionCategory7
from additioncategories import AdditionCategory8      

class AdditionErrorClassifier:
    
    scope = ""
    creds = ""
    client = ""
    sheet = ""
    uid = -1
    sheet_name = ""
    row_number = -1
    answer_by_user = -1
    number1 = -1
    number2 = -1
    number_of_questions_generated = -1
    number_of_numbers_in_each_question = -1
    
    def __init__(self, user_id, row, ans):
        
        self.uid = user_id
        self.sheet_name = "MSU" + str(self.uid)
        self.row_number = row
        
        self.scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('mathest.json', self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open(self.sheet_name).get_worksheet(0)
        
        self.number1 = int(self.sheet.cell(self.row_number, 1).value)
        self.number2 = int(self.sheet.cell(self.row_number, 2).value)
        self.answer_by_user = int(ans)
        
        self.number_of_questions_generated = 3
        self.number_of_numbers_in_each_question = 2
        
    def checkIfCorrect(cls):

        message = "Correct"
        if cls.number1 + cls.number2 != cls.answer_by_user:
            message = cls.classify()
        cls.sheet.update_cell(cls.row_number, 3, cls.answer_by_user)
        message_to_user = [
                {   'uid': cls.uid,
                    'comment': message
                }
        ]
        return message_to_user
        
    def classify(cls):
        
        """pp = pprint.PrettyPrinter()
        pp.pprint(number1)
        pp.pprint(number2)
        pp.pprint(answer_by_user)"""
        
        category_found = False
        original_list = []
        original_list.append(cls.number1)
        original_list.append(cls.number2)
        
        if category_found == False:
            ac1 = AdditionCategory1(original_list)
            if ac1.generate_answer() == cls.answer_by_user:
                category_found = True
                cls.sheet.update_cell(cls.row_number, 4, "1")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac1.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                return ac1.display_message()
        
        if category_found == False:
            ac2 = AdditionCategory2(original_list)
            if ac2.is_category_condition_satisfied() == True:
                answers = ac2.generate_answer()
                for i in range(len(answers)):
                    if answers[i] == cls.answer_by_user:
                        category_found = True
                if category_found == True:
                    cls.sheet.update_cell(cls.row_number, 4, "2")
                    for i in range(cls.number_of_questions_generated):
                        question_generated = ac2.generate_question(cls.number_of_numbers_in_each_question)
                        cls.sheet.append_row(question_generated)
                    return ac2.display_message()
        
        if category_found == False:
            ac3 = AdditionCategory3(original_list)
            if ac3.is_category_condition_satisfied() == True and ac3.generate_answer() == cls.answer_by_user:
                category_found = True
                cls.sheet.update_cell(cls.row_number, 4, "3")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac3.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                return ac3.display_message()
        
        if category_found == False:
            ac4 = AdditionCategory4(original_list)
            if ac4.is_category_condition_satisfied() == True and ac4.generate_answer() == cls.answer_by_user:
                category_found = True
                cls.sheet.update_cell(cls.row_number, 4, "4")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac4.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                return ac4.display_message()
        
        if category_found == False:
            ac5 = AdditionCategory5(original_list)
            if ac5.is_category_condition_satisfied() == True and ac5.generate_answer() == cls.answer_by_user:
                category_found = True
                cls.sheet.update_cell(cls.row_number, 4, "5")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac5.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                return ac5.display_message()
        
        if category_found == False:
            ac6 = AdditionCategory6(original_list)
            if ac6.is_category_condition_satisfied() == True and ac6.generate_answer() == cls.answer_by_user:
                category_found = True
                cls.sheet.update_cell(cls.row_number, 4, "6")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac6.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                return ac6.display_message()
        
        if category_found == False:
            ac7 = AdditionCategory7(original_list)
            if ac7.is_category_condition_satisfied() == True and ac7.generate_answer() == cls.answer_by_user:
                category_found = True
                cls.sheet.update_cell(cls.row_number, 4, "7")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac7.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                return ac7.display_message()
        
        if category_found == False:            
            ac8 = AdditionCategory8(original_list)
            if ac8.is_category_condition_satisfied() == True and ac8.generate_answer() == cls.answer_by_user:
                category_found = True
                cls.sheet.update_cell(cls.row_number, 4, "8")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac8.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                return ac8.display_message()
                    
        if category_found == False:
            random_questions = []
            category_found = True
            cls.sheet.update_cell(cls.row_number, 4, "X")
            for i in range(cls.number_of_questions_generated):
                random_questions.append(random.randint(1, 8))
            for i in range(cls.number_of_questions_generated):
                if random_questions[i] == 1:
                    question_generated = ac1.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                elif random_questions[i] == 2:
                    question_generated = ac2.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)    
                elif random_questions[i] == 3:
                    question_generated = ac3.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)    
                elif random_questions[i] == 4:
                    question_generated = ac4.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)    
                elif random_questions[i] == 5:
                    question_generated = ac5.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)    
                elif random_questions[i] == 6:
                    question_generated = ac6.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)    
                elif random_questions[i] == 7:
                    question_generated = ac7.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)    
                elif random_questions[i] == 8:
                    question_generated = ac8.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
            return "comment_random"
            #return "We couldn't classify the mistake you have made. But the correct answer to the problem is " + str(cls.number1 + cls.number2) + ". We are adding 3 more random questions keeping in mind that you went wrong for this question."
