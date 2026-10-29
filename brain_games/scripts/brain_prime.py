from brain_games.engine import run_game
from brain_games.games.prime import DESCRIPTION, get_prime_game_data


def main():

    run_game(DESCRIPTION, get_prime_game_data)

if __name__ == "__main__":
    main()