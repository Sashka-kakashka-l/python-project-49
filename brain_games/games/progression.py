import random

MIN_START = 1
MAX_START = 100
MIN_STEP = 1
MAX_STEP = 10
LENGTH = 10

DESCRIPTION = 'What number is missing in the progression?'

def get_progression_game_data():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)

    progression = [start + i * step for i in range(LENGTH)]

    hidden_index = random.randint(0, LENGTH - 1)

    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))

    return question, correct_answer