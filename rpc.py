import random

def get_user_choice():
    
    print("Rock -> 0, Paper -> 2, Scissors -> 5\nAny number except 0,2,5 to Quit the game")
    choice = input("Enter your choice: ")
    return choice
    

def get_computer_choice():
    return random.choice(['0', '2', '5'])


def determine_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == '0' and computer_choice == '2') or \
       (user_choice == '2' and computer_choice == '5') or \
       (user_choice == '5' and computer_choice == '2'):
        return "You win!"
    return "You lose!"


def play_game():
    
    user_score = 0
    computer_score = 0
    while True:
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        if user_choice not in ['0', '2', '5']:
            
            break

        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        if result == "You win!":
            user_score += 1
            print(f"You win this round")
        elif result == "You lose!":
            computer_score += 1
            print(f"You lose this round")
        print(f"\nScore:\nYou: {user_score}, Computer: {computer_score}\n\n")
    print(f"\nFinal Score:\nYou: {user_score}\nComputer: {computer_score}")
    if user_score > computer_score:
        print("You are the champion!")
    elif computer_score > user_score:
        print("Computer is the champion!")
    else:
        print("It's a tie!")

# Start the game
play_game()


            