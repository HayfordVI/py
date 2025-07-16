import random as rd

while True:
    user_choice = input('Rock, paper, scissors? (r/p/s) ')

    game_choices = ["r", "p", "s"]
    opponent_choice = (rd.choice(game_choices))

    if user_choice == 'r' and opponent_choice == 'p':
        print('You chose 🪨')
        print('The opps chose 📃')
        print("you lose")
    elif user_choice == 'r' and opponent_choice == 's':
        print('You chose 🪨')
        print('The opps chose ✂️')
        print('You win')
    elif user_choice == 'p' and opponent_choice == 'r':
        print('You chose 📃')
        print('The opps chose 🪨')
        print('You win')
    elif user_choice == 'p' and opponent_choice == 's':
        print('You chose 📃')
        print('The opps chose ✂️')
        print('You lose')
    elif user_choice == 's' and opponent_choice == 'p':
        print('You chose ✂️')
        print('The opps chose 📃')
        print('You win')
    elif user_choice == 's' and opponent_choice == 'r':
        print('You chose ✂️')
        print('The opps chose 🪨')
        print('You lose')
    elif user_choice == opponent_choice:
        print('It is a tie')
    else:
        print('Invalid choice')

    after_game = input('Continue? (y/n) ')
    if after_game == 'y':
        pass
    elif after_game == 'n':
        break
    else:
        print('Invalid choice')

# the program must pick one at random
# must program the hierarchy
# the option to terminate the game after one round
