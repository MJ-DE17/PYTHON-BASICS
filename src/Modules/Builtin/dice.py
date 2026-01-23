import random


def raandom(lst):
    print(random.choice(lst))

def dice(n):
    for i in range(10):
        print(random.randint(1,6))
