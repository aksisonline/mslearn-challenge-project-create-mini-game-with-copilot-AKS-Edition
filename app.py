import random

# Set up game variables
rock_emoji = "🪨"
paper_emoji = "📄"
scissors_emoji = "✂️"
player_choice = None
computer_choice = None

# Game loop
running = True
while running:
    # Get player's choice
    print("Choose your move:")
    print("1. Rock", rock_emoji)
    print("2. Paper", paper_emoji)
    print("3. Scissors", scissors_emoji)
    player_choice = input("Enter your choice (rock, paper, or scissors): ")

    # Generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Update game state
    if player_choice and computer_choice:
        # Determine the winner
        if player_choice == computer_choice:
            winner = "It's a tie!"
        elif ((player_choice == "rock" or player_choice == "1") and computer_choice == "scissors") or \
             ((player_choice == "paper" or player_choice == "2") and computer_choice == "rock") or \
             ((player_choice == "scissors" or player_choice == "3") and computer_choice == "paper"):
            winner = "Player wins!"
        else:
            winner = "Computer wins!"

        # Show the winner
        print(winner)
    else:
        # Render game state
        print("Choose your move:")
        print("1. Rock", rock_emoji)
        print("2. Paper", paper_emoji)
        print("3. Scissors", scissors_emoji)

# Clean up
