import random

items = ["apple", "banana", "orange", "grape", "book", "pencil"]

chosen_item = random.choice(items)

user_guess = input("Guess the item I'm thinking of: ")

if user_guess.lower() == chosen_item:  
  print("You guessed correctly! It was", chosen_item)
else:
  print("Sorry, that wasn't it. The item was", chosen_item)