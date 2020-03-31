from ..engine import play
from ..games.gcd import rules, generator


def main():
    play(rules, generator)


if __name__ == "__main__":
    main()
