from random import randint

print(":: Rock, Paper, Scissors App ::\n")

rounds = int(input("How many rounds of Rock, Paper, Scissors would you like to play?\n"))

moves = ["rock", "paper", "scissors"]

players_score = 0
computers_score = 0
print("Your moves Rock, Paper, Scissors.\n")

for x in range(rounds):
    your_move = input("Please select your move:\n").lower()

    computers_move = randint(0, 2)

    if moves[computers_move] == your_move:
        print("You both selected {0} its a draw\n".format(your_move))
    else:
        if your_move == "scissors" and moves[computers_move] == "paper":
            players_score += 1
            print("Your {0} beat the computers {1}\n".format(your_move, moves[computers_move]))
        elif your_move == "scissors" and moves[computers_move] == "rock":
            computers_score += 1
            print("Your {0} lost to the computers {1}\n".format(your_move, moves[computers_move]))
        elif your_move == "rock" and moves[computers_move] == "scissors":
            players_score += 1
            print("Your {0} beat the computers {1}\n".format(your_move, moves[computers_move]))
        elif your_move == "rock" and moves[computers_move] == "paper":
            computers_score += 1
            print("Your {0} lost to the computers {1}\n".format(your_move, moves[computers_move]))
        elif your_move == "paper" and moves[computers_move] == "rock":
            players_score += 1
            print("Your {0} beat the computers {1}\n".format(your_move, moves[computers_move]))
        else:
            computers_score += 1
            print("Your {0} lost to the computers {1}\n".format(your_move, moves[computers_move]))

print(":: The final score is ::\n")

print("\tPlayers score: {0}".format(players_score))
print("\tThe Computers Score is: {0}\n".format(computers_score))

if players_score > computers_score:
    print("\tYou won!")
elif players_score == computers_score:
    print("\tIts a draw!!")
else:
    print("\tComputers Wins!")