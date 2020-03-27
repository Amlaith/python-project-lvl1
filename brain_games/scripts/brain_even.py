from ..engine import play
from ..games.even import even_generator, rules


def main():
    play(even_generator, rules)


if __name__ == "__main__":
    main()
