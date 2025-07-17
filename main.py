# import random as rd

# while True:
#     user_choice = input('Rock, paper, scissors? (r/p/s) ')

#     game_choices = ["r", "p", "s"]
#     opponent_choice = (rd.choice(game_choices))

#     if user_choice == 'r' and opponent_choice == 'p':
#         print('You chose 🪨')
#         print('The opps chose 📃')
#         print("you lose")
#     elif user_choice == 'r' and opponent_choice == 's':
#         print('You chose 🪨')
#         print('The opps chose ✂️')
#         print('You win')
#     elif user_choice == 'p' and opponent_choice == 'r':
#         print('You chose 📃')
#         print('The opps chose 🪨')
#         print('You win')
#     elif user_choice == 'p' and opponent_choice == 's':
#         print('You chose 📃')
#         print('The opps chose ✂️')
#         print('You lose')
#     elif user_choice == 's' and opponent_choice == 'p':
#         print('You chose ✂️')
#         print('The opps chose 📃')
#         print('You win')
#     elif user_choice == 's' and opponent_choice == 'r':
#         print('You chose ✂️')
#         print('The opps chose 🪨')
#         print('You lose')
#     elif user_choice == opponent_choice:
#         print('It is a tie')
#     else:
#         print('Invalid choice')

#     after_game = input('Continue? (y/n) ')
#     if after_game == 'y':
#         pass
#     elif after_game == 'n':
#         break
#     else:
#         print('Invalid choice')


# better solution
import random as rd

emojis = {'r': '🪨',  'p': '📃', 's': '✂️'}
choices = ('r', 'p', 's')


while True:
    user_choice = input('Rock, paper, scissors? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invalid choice')
        continue

    computer_choice = rd.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie')
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
            (user_choice == 's' and computer_choice == 'p')):
        print("You win")
    else:
        print('You lose')

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break
