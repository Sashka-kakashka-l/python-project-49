from brain_games.engine import run_game
from brain_games.games.prime import get_prime_game_data


def main():
    rule = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'
    run_game(rule, get_prime_game_data)

if __name__ == "__main__":
    main()