import random
import operator


RULES = "What is the result of the expression?"
OPERATORS = (("+", operator.add), ("*", operator.mul), ("-", operator.sub))


def generate_round():
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    operator_sign, operator_function = random.choice(OPERATORS)
    question = " ".join((str(a), operator_sign, str(b)))
    answer = str(operator_function(a, b))
    return (question, answer)
