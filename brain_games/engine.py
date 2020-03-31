from .cli import print_welcome, welcome_user


def play(game):
    print_welcome()
    print(game.RULES)

    print()

    name = welcome_user()

    print()

    correct_acc = 0
    while correct_acc < 3:
        question, answer = game.generator()
        print("Question: " + question)
        guess = input("Your answer: ")
        if guess == answer:
            print("Correct!")
            correct_acc = correct_acc + 1
            continue
        print(
            "'{}' is wrong answer ;(. Correct answer was '{}'."
            .format(guess, answer)
            )
        print("Let's try again, {}!".format(name))
        return None
    print("Congratulations, {}!".format(name))
