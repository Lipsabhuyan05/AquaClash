import random

def get_winner(user, computer):
    """
    Returns:
    'win', 'lose', or 'draw'
    """
    if user == computer:
        return "draw"

    rules = {
        "snake": "water",   # snake drinks water
        "water": "gun",     # water damages gun
        "gun": "snake"      # gun kills snake
    }

    if rules[user] == computer:
        return "win"
    else:
        return "lose"


def play_game():
    print("Welcome to AquaClash!")
    print("Rules:")
    print("Snake drinks Water")
    print("Water damages Gun")
    print("Gun kills Snake\n")

    rounds = int(input("Enter number of rounds you want to play: "))

    options = ["snake", "water", "gun"]
    user_score = 0
    computer_score = 0

    for round_no in range(1, rounds + 1):
        print(f"\nRound {round_no}")
        user = input("Choose Snake / Water / Gun: ").lower()

        if user not in options:
            print("Invalid choice! Round skipped.")
            continue

        computer = random.choice(options)
        print(f"Computer chose: {computer}")

        result = get_winner(user, computer)

        if result == "win":
            print("You Win this round!")
            user_score += 1
        elif result == "lose":
            print("You Lose this round!")
            computer_score += 1
        else:
            print("It's a Draw!")

    print("\nFinal Score")
    print(f"You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You won AquaClash!")
    elif user_score < computer_score:
        print("Computer wins AquaClash!")
    else:
        print("Match Draw!")


# Run the game
play_game()
