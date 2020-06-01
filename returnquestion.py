import gspread
from oauth2client.service_account import ServiceAccountCredentials

class ReturnQuestion:
    
    uid = -1
    row_number = -1
    sheet_number = -1
    
    def __init__(self, user_id, row, sno):
        
        self.uid = user_id
        self.row_number = row
        self.sheet_number = int(sno)
        
    def getNextQuestion(cls):
        
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('mathest.json', scope)
        client = gspread.authorize(creds)
        sheet_name = "MSU" + str(cls.uid)

        sheet = client.open(sheet_name)
        
        if cls.sheet_number == 1:
            work_sheet = sheet.get_worksheet(0)
        elif cls.sheet_number == 2:
            work_sheet = sheet.get_worksheet(1)
        elif cls.sheet_number == 3:
            work_sheet = sheet.get_worksheet(2)
        elif cls.sheet_number == 4:
            work_sheet = sheet.get_worksheet(3)
        
        number1 = work_sheet.cell(cls.row_number, 1).value
        number2 = work_sheet.cell(cls.row_number, 2).value

        if number1 != '' and number2 != '':
            question = [
                    {
                        'uid': cls.uid,
                        'number1': int(number1),
                        'number2': int(number2)
                    }
            ]
        else:
            question = [
                    {
                        'error': "NaN"
                    }
            ]
        
        return question;
