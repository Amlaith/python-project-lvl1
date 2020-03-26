from random import randint


def play(name):
    answers = {
        0: "yes",
        1: "no",
    }
    correct_acc = 0
    while correct_acc < 3:
        num = randint(1, 100)
        print("Question:", num)
        guess = input("Your answer: ")
        answer = answers[num % 2]
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
