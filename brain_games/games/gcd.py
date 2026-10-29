import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_START = 1
MAX_START = 100

def get_gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def get_gcd_game_data():
    num1 = random.randint(MIN_START, MAX_START)
    num2 = random.randint(MIN_START, MAX_START)

    question = f"{num1} {num2}"
    correct_answer = str(get_gcd(num1, num2))

    return question, correct_answer