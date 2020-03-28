from ..engine import play
from ..games.progression import rules, progression_generator


def main():
    play(rules, progression_generator)


if __name__ == '__main__':
    main()
