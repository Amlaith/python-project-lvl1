from random import randint


RULES = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while True:
        a, b = max(a, b), min(a, b)
        a = a % b
        if a == 0:
            return b


def generate_round():
    a = randint(1, 101)
    b = randint(1, 101)
    question = "{} {}".format(str(a), str(b))
    answer = str(gcd(a, b))
    return question, answer
