from ..engine import play
from ..games.calc import generator, rules


def main():
    play(rules, generator)


if __name__ == "__main__":
    main()
