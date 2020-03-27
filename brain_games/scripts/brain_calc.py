from ..engine import play
from ..games.calc import calc_generator, rules


def main():
    play(calc_generator, rules)


if __name__ == "__main__":
    main()
