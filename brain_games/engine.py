import prompt

from brain_games.cli import welcome_user

ROUND_COUNT = 3

def run_game(game_rule, get_game_data):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(game_rule)

    for _ in range(ROUND_COUNT):
        question, correct_answer = get_game_data()
        print(f"Qestion: {question}")

        user_answer = prompt.string("Your answer:")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;"
                  f"(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
