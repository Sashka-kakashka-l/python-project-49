from brain_games.engine import run_game
from brain_games.games.even import DESCRIPTION, get_even_game_data


def main():
    run_game(DESCRIPTION, get_even_game_data)

if __name__ == "__main__":
    main()