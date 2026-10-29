from brain_games.engine import run_game
from brain_games.games.gcd import DESCRIPTION, get_gcd_game_data


def main():

    run_game(DESCRIPTION, get_gcd_game_data)

if __name__ == "__main__":
    main()