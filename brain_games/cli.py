import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def print_welcome():
    print('Welcome to the Brain Games!')
