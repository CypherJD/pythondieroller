from random import randint

Die_side = int(input("What side die do you want to roll?"))

repeat = True
while repeat:
    print("You rolled a...",randint(1, Die_side))
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()
