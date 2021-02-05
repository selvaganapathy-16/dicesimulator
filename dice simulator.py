import random

y = "r"
while y == "r":
    x = random.randint(1, 6)

    if x == 1:
        print('--------------')
        print('|            |')
        print('|            |')
        print('|     0      |')
        print('|            |')
        print('|            |')
        print('--------------')
    if x == 2:
        print('--------------')
        print('|            |')
        print('|     0      |')
        print('|            |')
        print('|     0      |')
        print('|            |')
        print('--------------')
    if x == 3:
        print('--------------')
        print('|      0     |')
        print('|            |')
        print('|      0     |')
        print('|            |')
        print('|      0     |')
        print('--------------')
    if x == 4:
        print('--------------')
        print('| 0        0 |')
        print('|            |')
        print('|            |')
        print('|            |')
        print('| 0        0 |')
        print('--------------')
    if x == 5:
        print('--------------')
        print('| 0        0 |')
        print('|            |')
        print('|     0      |')
        print('|            |')
        print('| 0        0 |')
        print('--------------')
    if x == 6:
        print('--------------')
        print('| 0        0 |')
        print('|            |')
        print('| 0        0 |')
        print('|            |')
        print('| 0        0 |')
        print('--------------')
    y = input("press r to roll the dice again")
    print("\n")
