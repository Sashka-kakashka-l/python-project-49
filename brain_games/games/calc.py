import random
from operator import add, mul, sub

DESCRIPTION = 'What is the result of the expression?'

MIN_NUM = 1
MAX_NUM = 50
OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
}


def calculate(num1, operator, num2):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2


def get_calc_game_data():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    operator = random.choice(['+', '-', '*'])

    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculate(num1, operator, num2))

    return question, correct_answer