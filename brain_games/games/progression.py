import random






def get_progression_game_data():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    length = 10

    for _ in range(length):
        lists = [start + i * step for i in range(length)]

    c = random.randint(1, 9)

    correct_answer = str((lists[c]))
    lists[c] = ".."
    question = f"{lists}"

    return question, correct_answer