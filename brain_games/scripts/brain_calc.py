from ..engine import play
from ..games.calc import calc_generator, rules


def main():
    play(rules, calc_generator)


if __name__ == "__main__":
    main()
