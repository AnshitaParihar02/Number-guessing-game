import random

def welcome_message():
    print("\n" + "="*40)
    print("  Welcome to the Number Guessing Game! ")
    print("="*40)
    print("I have selected a number between 1 and 100.")
    print("Your goal is to guess the number correctly.")
    print("You will receive hints if your guess is too high or too low.")
    print("Let's begin!\n")

def choose_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy (15 attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard (5 attempts)")
    
    while True:
        try:
            choice = int(input("Enter 1, 2, or 3: "))
            if choice == 1:
                return 15
            elif choice == 2:
                return 10
            elif choice == 3:
                return 5
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = choose_difficulty()
    attempts = 0

    print(f"\nYou have {max_attempts} attempts to guess the number.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:
                print(f" Congratulations! You guessed the number in {attempts} attempts! ")
                break
        except ValueError:
            print(" Please enter a valid number.\n")

    if attempts == max_attempts and guess != secret_number:
        print(f" Sorry! You've used all {max_attempts} attempts. The number was {secret_number}.\n")

def main():
    while True:
        welcome_message()
        play_game()
        
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break


main()
