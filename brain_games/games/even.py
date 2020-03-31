from random import randint


RULES = "Answer \"yes\" if number is even, otherwise answer \"no\"."


def generator():
    answers = {
        0: "yes",
        1: "no",
    }
    num = randint(1, 100)
    question = str(num)
    answer = answers[num % 2]
    return question, answer
