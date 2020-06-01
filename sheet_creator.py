import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials 

#class to create a sheet
#Requires uid of the user
class SheetCreator:
    scope =  ""
    creds = ""
    gc = ""

    #constructor to initialize the necessary components
    def __init__(self):
        self.scope =  ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('mathest.json', self.scope)
        self.gc = gspread.authorize(self.creds) 

    #function to be called to create a sheet, return id of the sheet
    #The sheet title would be of the form MSU<UID_sent> 
    def create_sheet(cls, uid):
        print(uid)
        original_sheet = cls.gc.open('Main_Sheet')
        sheet_title = 'MSU' + str(uid)
        new_sheet = cls.gc.copy(file_id = original_sheet.id, title = sheet_title, copy_permissions = True)
        #cls.generate_questions(new_sheet, 0)
        new_sheet.share('cse.mobilecomputingforum@gmail.com', perm_type = 'user', role = 'writer')
        sheet = [
                {   'uid': uid,
                    'id': new_sheet.id
                }
        ]
        return sheet

    def generate_questions(cls, new_sheet, sheetNo):
        count = 0
        while count != 10:
            number1 = random.randint(0, 999)
            number2 = random.randint(0, 999)
            work_sheet = new_sheet.get_worksheet(sheetNo)
            work_sheet.update_cell((count + 2), 1, number1)
            work_sheet.update_cell((count + 2), 2, number2)
            count = count + 1
