from brain_games.cli import print_welcome, welcome_user
import prompt


def play(game):
    print_welcome()
    print(game.RULES)

    print()

    name = welcome_user()

    print()

    ROUNDS = 3
    correct_acc = 0
    while correct_acc < ROUNDS:
        question, answer = game.generate_round()
        print("Question: " + question)
        guess = prompt.string("Your answer: ")
        if guess == answer:
            print("Correct!")
            correct_acc = correct_acc + 1
            continue
        print(
            "'{}' is wrong answer ;(. Correct answer was '{}'."
            .format(guess, answer)
            )
        print("Let's try again, {}!".format(name))
        return
    print("Congratulations, {}!".format(name))
