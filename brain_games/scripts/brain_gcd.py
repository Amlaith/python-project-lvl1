from ..engine import play
from ..games.gcd import rules, gcd_generator


def main():
    play(rules, gcd_generator)


if __name__ == "__main__":
    main()
