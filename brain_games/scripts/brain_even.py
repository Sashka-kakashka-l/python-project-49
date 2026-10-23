from brain_games.engine import run_game
from brain_games.games.even import get_even_game_data


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(rule, get_even_game_data)

if __name__ == "__main__":
    main()