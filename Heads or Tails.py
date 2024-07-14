# Heads or Tails
import random

print("Welcome to Heads or Tails")
print("Please choose Heads or Tails")
choice = input ( "Enter your choice:")
print("You have chosen", choice)
print("Now the coin is tossed")
coin = random.randint(1,2)
if coin == 1:
  print("Heads")
elif coin == 2:
  print("Tails")
if coin == 1 and choice == "Heads":
  print("You win")
if coin == 2 and choice == "Tails":
  print("You win")
if coin == 1 and choice == "Tails":
  print("You lose")
if coin == 2 and choice == "Heads":
  print("You lose")


