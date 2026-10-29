from brain_games.engine import run_game
from brain_games.games.calc import DESCRIPTION, get_calc_game_data


def main():

    run_game(DESCRIPTION, get_calc_game_data)

if __name__ == "__main__":
    main()