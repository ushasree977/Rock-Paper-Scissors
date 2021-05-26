import random

comp_wins = 0
player_wins = 0


def choose_option():
    user_choice = input("choose Rcck,Paper or Scissor :\n")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in {"Paper", "paper", "p", "P"}:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        choose_option()
    return user_choice

def computer_option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")
    user_choice = choose_option()
    comp_choice = computer_option()
    print("")
    if user_choice == "r":
        if comp_choice == "r":
            print("You choose rock. The compute choose rock. You tied.")
        elif comp_choice == "p":
            print("You choose rock. The computer choose paper. You lose.")
            comp_wins += 1
        elif comp_choice == "s":
            print("You choose rock. The computer choose scissors. You win.")
            player_wins += 1
    elif user_choice == "p":
        if comp_choice == "r":
            print("You choose paper. The computer choose rock. You win")
            player_wins += 1
        elif comp_choice == "p":
            print("You choose paper. The computer choose paper. You tied")
        elif comp_choice == "s":
            print("You choose paper. The computer choose scissors. You lose")
            comp_wins += 1
    elif user_choice == "s":
        if comp_choice == 'r':
            print("You choose scissors. The computer choose rock. You lose.")
            comp_wins += 1
        elif comp_choice == "p":
            print("You choose scissors. The computer choose scissors. You tied")
            player_wins += 1
        elif comp_choice == "s":
            print("You choose scissors. The computer choose scissors. You tied")

    print("")
    print("player wins : " + str(player_wins))
    print("comp wins : " + str(comp_wins))
    print("")
    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "Yes","yes"]:
        pass
    elif user_choice in ["N", "n", "No", "no"]:
        break
    else:
        break


