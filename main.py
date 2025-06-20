import random

while True:
    player = input("Roll the dice? (y/n): ")
    if player.casefold() == "y":
        answer = random.randrange(1, 6)
        answero = random.randrange(1, 6)
        print(f'({answero}, {answer})')
    elif player.casefold() == "n":
        print("Thanks for playing!")
        break
    else:
        print('Invalid choice!')
