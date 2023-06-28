import random


def choose_one(values: [int]):
    total_val = 0
    for i in values:
        total_val += i
    num = random.randint(0, total_val)

    number_on = 0
    index = 0
    for i in values:
        if num <= i + number_on:
            return index
        else:
            number_on += i
        index += 1
