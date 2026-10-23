from brain_games.engine import run_game
from brain_games.games.progression import get_progression_game_data


def main():
    rule = 'What number is missing in the progression?'
    run_game(rule, get_progression_game_data)

if __name__ == "__main__":
    main()