from brain_games.engine import run_game
from brain_games.games.gcd import get_gcd_game_data


def main():
    rule = 'Find the greatest common divisor of given numbers.'
    run_game(rule, get_gcd_game_data)

if __name__ == "__main__":
    main()