import random
computer_number = random.randint(0, 999999)

while True:
    player_input = input("Guess the number (0-999999): ")
    if not player_input.isdigit():
        print("Please enter a valid number...")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print("You win!")
        break
    elif player_number > computer_number:
        print("Too high!")
    else:
        print("Too low!")