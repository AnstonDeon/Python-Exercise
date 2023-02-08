import random
# define the rules of the game
print("Welcome to Snake Water Gun!")
print("In this game, you will choose either 'snake', 'water', or 'gun'.")
print("If both players choose the same option, the round is a tie.")
print("If one player chooses 'snake' and the other chooses 'water', the player who chose 'snake' wins.")
print("If one player chooses 'snake' and the other chooses 'gun', the player who chose 'gun' wins.")
print("If one player chooses 'water' and the other chooses 'gun', the player who chose 'water' wins.")

# initialize the scores
player_score = 0
computer_score = 0

# create a loop for the game to run
while True:
    # get player choice
    player_choice = input("Choose 'snake', 'water', or 'gun': ")
    # get computer choice
    computer_choice = random.choice(['snake', 'water', 'gun'])
    # determine the outcome of the round
    if player_choice == computer_choice:
        print("Tie!")
    elif (player_choice == 'snake' and computer_choice == 'water') or (player_choice == 'water' and computer_choice == 'gun') or (player_choice == 'gun' and computer_choice == 'snake'):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    # print the scores
    print(f"Player: {player_score} Computer: {computer_score}")
    # check if the player wants to play again
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() == 'no':
        break
