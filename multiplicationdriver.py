import gspread
#import pprint
from oauth2client.service_account import ServiceAccountCredentials
import random
from multiplicationcategories import MultiplicationCategory1 
from multiplicationcategories import MultiplicationCategory2 
from multiplicationcategories import MultiplicationCategory3
from multiplicationcategories import MultiplicationCategory4    

class MultiplicationErrorClassifier:
    
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
        self.sheet = self.client.open(self.sheet_name).get_worksheet(2)
        
        self.number1 = int(self.sheet.cell(self.row_number, 1).value)
        self.number2 = int(self.sheet.cell(self.row_number, 2).value)
        
        self.answer_by_user = int(ans)
        
        self.number_of_questions_generated = 3
        self.number_of_numbers_in_each_question = 2
        
    def checkIfCorrect(cls):

        message = "Correct"
        if cls.number1 * cls.number2 != cls.answer_by_user:
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
            mc1 = MultiplicationCategory1(original_list)
            if mc1.is_category_condition_satisfied() == True:
                answers = mc1.generate_answer()
                for i in range(len(answers)):
                    if answers[i] == cls.answer_by_user:
                        category_found = True
                if category_found == True:
                    cls.sheet.update_cell(cls.row_number, 4, "1")
                    for i in range(cls.number_of_questions_generated):
                        question_generated = mc1.generate_question(cls.number_of_numbers_in_each_question)
                        cls.sheet.append_row(question_generated)
                    return mc1.display_message()
                
        if category_found == False:
            mc2 = MultiplicationCategory2(original_list)
            if mc2.generate_answer() == cls.answer_by_user:
                category_found = True
                cls.sheet.update_cell(cls.row_number, 4, "2")
                for i in range(cls.number_of_questions_generated):
                    question_generated = mc2.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                return mc2.display_message()
            
        if category_found == False:
            mc3 = MultiplicationCategory3(original_list)
            if mc3.is_category_condition_satisfied() == True:
                answers = mc3.generate_answer()
                for i in range(len(answers)):
                    if answers[i] == cls.answer_by_user:
                        category_found = True
                if category_found == True:
                    cls.sheet.update_cell(cls.row_number, 4, "3")
                    for i in range(cls.number_of_questions_generated):
                        question_generated = mc3.generate_question(cls.number_of_numbers_in_each_question)
                        cls.sheet.append_row(question_generated)
                    return mc3.display_message()
                
        if category_found == False:
            mc4 = MultiplicationCategory4(original_list)
            if mc4.is_category_condition_satisfied() == True and mc4.generate_answer() == cls.answer_by_user:
                category_found = True
                cls.sheet.update_cell(cls.row_number, 4, "4")
                for i in range(cls.number_of_questions_generated):
                    question_generated = mc4.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                return mc4.display_message()
        
        if category_found == False:
            random_questions = []
            category_found = True
            cls.sheet.update_cell(cls.row_number, 4, "X")
            for i in range(cls.number_of_questions_generated):
                random_questions.append(random.randint(1, 4))
            for i in range(cls.number_of_questions_generated):
                if random_questions[i] == 1:
                    question_generated = mc1.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                elif random_questions[i] == 2:
                    question_generated = mc2.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)    
                elif random_questions[i] == 3:
                    question_generated = mc3.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
                elif random_questions[i] == 4:
                    question_generated = mc4.generate_question(cls.number_of_numbers_in_each_question)
                    cls.sheet.append_row(question_generated)
            return "comment_random"
            #return "We couldn't classify the mistake you have made. But the correct answer to the problem is " + str(cls.number1 * cls.number2) + ". We are adding 3 more random questions keeping in mind that you went wrong for this question."
