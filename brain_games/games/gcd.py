from random import randint
from math import gcd


rules = "Find the greatest common divisor of given numbers."


def gcd_generator():
    a = randint(1, 101)
    b = randint(1, 101)
    question = " ".join((str(a), str(b)))
    answer = str(gcd(a, b))
    return question, answer
