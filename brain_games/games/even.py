from random import randint


rules = "Answer \"yes\" if number even otherwise answer \"no\"."


def even_generator():
    answers = {
        0: "yes",
        1: "no",
    }
    num = randint(1, 100)
    question = str(num)
    answer = answers[num % 2]
    return question, answer
