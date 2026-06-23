import random

win_number = random.randint(1, 20)
player_guess = None
attempts = 0

print("Guess the number between 1 and 20!")

while player_guess != win_number:
    player_guess = int(input("Your player_guess: "))
    attempts += 1

    if player_guess < win_number:
        print("Too low!")
    elif player_guess > win_number:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts.")