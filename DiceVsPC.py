import random

def roll_dice():
    return random.randint(1, 6)

print("🎲 Welcome to the Dice Rolling Game!")

while True:
    input("Press Enter to roll the dice...")
    player_roll = roll_dice()
    computer_roll = roll_dice()

    print(f"You rolled: {player_roll}")
    print(f"Computer rolled: {computer_roll}")

    if player_roll > computer_roll:
        print("🎉 You win!")
    elif player_roll < computer_roll:
        print("😞 You lose.")
    else:
        print("🤝 It's a tie!")

    play_again = input("Roll again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
