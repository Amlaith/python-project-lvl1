from random import randint


rules = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def generator():
    question = randint(1, 100)
    for i in range(2, question):
        if question % i == 0:
            answer = "no"
            break
    else:
        answer = "yes"
    question = str(question)
    return question, answer
