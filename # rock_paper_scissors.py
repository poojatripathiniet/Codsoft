# rock_paper_scissors.py

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def show_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "tie":
        print("It's a TIE!")
    elif winner == "user":
        print("🎉 You WIN!")
    else:
        print("💻 Computer WINS!")

# Score tracking
user_score = 0
computer_score = 0

print("=== Welcome to Rock-Paper-Scissors Game ===")

while True:
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose again.")
        continue

    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    show_result(user_choice, computer_choice, winner)

    # Update scores
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

    print(f"Score => You: {user_score} | Computer: {computer_score}")

    # Ask to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break