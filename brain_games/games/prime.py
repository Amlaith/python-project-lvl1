from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    i = 2
    while i < num ** 0.5:
        if num % i == 0:
            return False
        i += 1
    return True


def generate_round():
    question = randint(1, 100)
    answer = "yes" if is_prime(question) else "no"
    question = str(question)
    return question, answer
