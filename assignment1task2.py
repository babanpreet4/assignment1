# Task 2: Rock-Paper-Scissors

# Accept input from both players
player1 = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
player2 = input("Player 2, enter your choice (rock/paper/scissors): ").lower()

# Valid choices
choices = ["rock", "paper", "scissors"]

# Check for invalid input
if player1 not in choices or player2 not in choices:
    print("Invalid input! Please choose rock, paper, or scissors.")
else:
    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
