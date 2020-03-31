from ..engine import play
from ..games.even import generator, rules


def main():
    play(rules, generator)


if __name__ == "__main__":
    main()
