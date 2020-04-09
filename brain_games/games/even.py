from random import randint


RULES = 'Answer "yes" if number is even, otherwise answer "no".'


def generate_round():
    num = randint(1, 100)
    question = str(num)
    answer = "no" if (num % 2) else "yes"
    return question, answer
