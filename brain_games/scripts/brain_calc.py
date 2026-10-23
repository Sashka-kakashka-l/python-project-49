from brain_games.engine import run_game
from brain_games.games.calc import get_calc_game_date


def main():
    rule = 'What is the result of the expression?'
    run_game(rule, get_calc_game_date)

if __name__ == "__main__":
    main()