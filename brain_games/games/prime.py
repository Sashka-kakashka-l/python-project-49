import random


def get_prime(num1):
    if num1 <= 1:
        return 'no'
    for i in range(2, num1):
        if num1 % i == 0:
            return 'no'

    return 'yes'


def get_prime_game_data():
    num1 = random.randint(1, 100)

    question = f"{num1}"
    correct_answer = str(get_prime(num1))

    return question, correct_answer