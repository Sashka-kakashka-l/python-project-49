import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_START = 1
MAX_START = 100

def is_even(number):
    return number % 2 == 0


def get_even_game_data():
    number = random.randint(MIN_START, MAX_START)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer