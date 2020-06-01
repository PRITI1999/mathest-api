"""
    author : Mrinal Pandey
             Priti Chattopadhyay
                                """
#importing necessary classes and packages
from returnquestion import ReturnQuestion
from sheet_creator import SheetCreator 
from additiondriver import AdditionErrorClassifier
from subtractiondriver import SubtractionErrorClassifier
from multiplicationdriver import MultiplicationErrorClassifier
from divisiondriver import DivisionErrorClassifier
from AdditionWorking import *
from MultiplicationWorking import *
import flask
from flask import request, jsonify, render_template

#Configuring the Flask Application
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ['GET'])
def hello():
    return render_template('index.html')

#format to call: "<base_url>/question?uid=<user_uid>&row=<next_row>&sno=<sheet_number>"
"""
    sheet_number = 1 for Addition, 2 for subtraction, 3 for multiplication and 4 for division
"""
@app.route('/question', methods = ['GET', 'POST'])
def returnNextQuestion():
    uid = request.args['uid']
    row_number = request.args['row']
    sheet = request.args['sno']
    return_question = ReturnQuestion(uid, row_number, sheet)
    return jsonify(return_question.getNextQuestion())

#format to call: "<base_url>/sheet?uid=<user_uid>"
@app.route('/sheet', methods = ['GET', 'POST'])
def returnNewSheet():
    uid = request.args['uid']
    new_sheet = SheetCreator()
    return jsonify(new_sheet.create_sheet(uid))

#format to call: "<base_url>/addition?uid=<user_uid>&row=<current_row>&answer=<answer_by_user>"
@app.route('/addition', methods = ['GET', 'POST'])
def addition():
    uid = request.args['uid']
    row_number = request.args['row']
    answer_by_user = request.args['answer']
    addition_error_classifier = AdditionErrorClassifier(uid, row_number, answer_by_user)
    return jsonify(addition_error_classifier.checkIfCorrect())

#format to call: "<base_url>/subtraction?uid=<user_uid>&row=<current_row>&answer=<answer_by_user>"
@app.route('/subtraction', methods = ['GET', 'POST'])
def subtraction():
    uid = request.args['uid']
    row_number = request.args['row']
    answer_by_user = request.args['answer']
    subtraction_error_classifier = SubtractionErrorClassifier(uid, row_number, answer_by_user)
    return jsonify(subtraction_error_classifier.checkIfCorrect())

#format to call: "<base_url>/multiplication?uid=<user_uid>&row=<current_row>&answer=<answer_by_user>"
@app.route('/multiplication', methods = ['GET', 'POST'])
def multiplication():
    uid = request.args['uid']
    row_number = request.args['row']
    answer_by_user = request.args['answer']
    multiplication_error_classifier = MultiplicationErrorClassifier(uid, row_number, answer_by_user)
    return jsonify(multiplication_error_classifier.checkIfCorrect())

#format to call: "<base_url>/division?uid=<user_uid>&row=<current_row>&answer=<answer_by_user>"
@app.route('/division', methods = ['GET', 'POST'])
def division():
    uid = request.args['uid']
    row_number = request.args['row']
    answer_by_user = request.args['answer']
    division_error_classifier = DivisionErrorClassifier(uid, row_number, answer_by_user)
    return jsonify(division_error_classifier.checkIfCorrect())
    
#format to call: "<base_url>/addition-working?uid=<user_uid>&number1=<first_number>&number2=<second_number>"
@app.route('/addition-working', methods = ['GET', 'POST'])
def workingOfAddition():
    uid = request.args['uid']
    number1 = request.args['number1']
    number2 = request.args['number2']
    return jsonify(addition_working(uid, number1, number2))

#format to call: "<base_url>/multiplication-working?uid=<user_uid>&number1=<first_number>&number2=<second_number>"
@app.route('/multiplication-working', methods = ['GET', 'POST'])
def workingOfMultiplication():
    uid = request.args['uid']
    number1 = request.args['number1']
    number2 = request.args['number2']
    return jsonify(multiplication_working(uid, number1, number2))

if __name__ == '__main__':
    app.run()
