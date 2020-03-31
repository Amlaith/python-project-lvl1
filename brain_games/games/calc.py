from random import randint, choice
from operator import add, mul, sub


rules = "What is the result of the expression?"


def generator():
    operators = ("+", "*", "-")
    operator_foos = {
        "+": add,
        "*": mul,
        "-": sub,
        }
    a = randint(0, 20)
    b = randint(0, 20)
    operator = choice(operators)
    question = " ".join((str(a), operator, str(b)))
    answer = str(operator_foos[operator](a, b))
    return question, answer
