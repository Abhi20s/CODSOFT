import random

def get_choice_name(choice):
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    elif choice == 3:
        return 'Scissors'
    return 'Invalid'

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return 'DRAW'
    elif (user_choice == 1 and comp_choice == 3) or \
         (user_choice == 2 and comp_choice == 1) or \
         (user_choice == 3 and comp_choice == 2):
        return 'USER'
    else:
        return 'COMPUTER'

def main():
    user_score = 0
    computer_score = 0

    print('Welcome to the Rock-Paper-Scissors Game!')
    print('Winning rules of the game are as follows:')
    print('- Rock beats Scissors')
    print('- Scissors beat Paper')
    print('- Paper beats Rock')

    while True:
        print("\nPlease make your choice:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")

        try:
            user_choice = int(input("Enter your choice (1/2/3): "))
            if user_choice not in [1, 2, 3]:
                print("Invalid choice. Please enter a number between 1 and 3.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number (1, 2, or 3).")
            continue

        user_choice_name = get_choice_name(user_choice)
        print(f'\nYou chose: {user_choice_name}')
        
        comp_choice = random.randint(1, 3)
        comp_choice_name = get_choice_name(comp_choice)
        print(f'The computer chose: {comp_choice_name}')

        result = determine_winner(user_choice, comp_choice)
        if result == 'DRAW':
            print("It's a tie!")
        elif result == 'USER':
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nCurrent Score: You {user_score} - Computer {computer_score}")

        play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing!")
            print(f"Final Score: You {user_score} - Computer {computer_score}")
            break

if __name__ == "__main__":
    main()