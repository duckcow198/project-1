import random # imports the random module so the computer can choose a random choice

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    player_score = 0 # starts player's score at 0
    computer_score = 0 # starts computer score at 0

    

    while True: # makes a loop to keep the game going until the player quits
        print("\nScore: Player: {} / Computer: {}".format(player_score, computer_score)) # displays score
        player_choice = input("Choose Rock, Paper, or Scissors (or type 'quit' to exit): ").lower() # asks player for their choice

        # checks if the player wants to quit and if so, ends the game and displays the final score
        if player_choice == "quit": 
            print("Thanks for playing! Final Score: Player: {} / Computer: {}".format(player_score, computer_score))
            break

        # if the player doesn't choose rock, paper, or scissors, then says invalid and regives the choice.
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        # computer randomly selects a choice then prints it
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        # decides who wins
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
# without this the game doesn't run properly
if __name__ == "__main__":
    play_game()
