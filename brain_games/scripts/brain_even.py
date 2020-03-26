from ..cli import welcome_user
from .brain_games import print_welcome
from ..even import play


def main():
    print_welcome()
    print("Answer \"yes\" if number even otherwise answer \"no\".")
    name = welcome_user()
    play(name)

if __name__ == "__main__":
    main()
