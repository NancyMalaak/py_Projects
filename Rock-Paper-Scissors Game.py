import random

rock = '''
    ___
---'   ____)
      (_)
      (_)
      (____)
---.(___)
'''

paper = '''
    ___
---'   __)__
          __)
          ___)
         ___)
---.__)
'''

scissors = '''
    ___
---'   __)__
          __)
       __)
      (____)
---.(___)
'''
game_images = [rock, paper, scissors]

user_score = 0
computer_score = 0

while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice >= 3 or user_choice < 0: 
        print("You typed an invalid number, you lose!") 
    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
            user_score += 1
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
            computer_score += 1
        elif computer_choice > user_choice:
            print("You lose")
            computer_score += 1
        elif user_choice > computer_choice:
            print("You win!")
            user_score += 1
        elif computer_choice == user_choice:
            print("It's a draw")

        print(f"Scores -> You: {user_score} Computer: {computer_score}")

    play_again = input("Do you want to play another round? Type 'yes' or 'no':\n")
    if play_again.lower() != 'yes':
        break

print("Thanks for playing!")