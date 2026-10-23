import random


def calc_eval(expression):
    return eval(expression)

def get_calc_game_date():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator =  random.choice(["+", "-", "*"])

    expression = f"{num1} {operator} {num2}"
    correct_answer = str(calc_eval(expression))
    return expression, correct_answer
