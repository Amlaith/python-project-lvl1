from random import randint


RULES = "What number is missing in the progression?"


def generator():
    start = randint(1, 10)
    step = randint(1, 10)

    sequence = [start + step * n for n in range(10)]

    missing = randint(0, 9)
    answer = str(sequence[missing])
    sequence[missing] = ".."
    question = " ".join(map(str, sequence))
    return question, answer
