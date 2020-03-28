from ..engine import play
from ..games.even import even_generator, rules


def main():
    play(rules, even_generator)


if __name__ == "__main__":
    main()
