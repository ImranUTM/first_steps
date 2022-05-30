import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["0", "1", "2"]
    computer_action = random.choice(possible_actions)


    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "0":
        if computer_action == "2":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "1":
        if computer_action == "0":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "2":
        if computer_action == "1":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

