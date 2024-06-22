# TASK-4 

'''
Rock Paper Scissor
'''

import random

# Function to display the menu and get the user's choice
def get_user_choice():
    print("Choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        return 'rock'
    elif choice == '2':
        return 'paper'
    elif choice == '3':
        return 'scissors'
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()

# Function to generate the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    choice = random.choice(choices)
    return choice

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            return "Rock beats Scissors. You win!"
        else:
            return "Paper beats Rock. You lose."
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            return "Paper beats Rock. You win!"
        else:
            return "Scissors beat Paper. You lose."
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            return "Scissors beat Paper. You win!"
        else:
            return "Rock beats Scissors. You lose."

# Function to display the results
def display_results(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

# Main function to control the game flow
def main():
    user_score = 0
    computer_score = 0
    playing = True
    
    while playing:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_results(user_choice, computer_choice, result)
        
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1
        
        print(f"Score: You {user_score} - {computer_score} Computer")
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            playing = False
    
    print("Thanks for playing! Goodbye!")

# Run the game
if __name__ == "__main__":
    main()
