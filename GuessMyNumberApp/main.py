from random import randint

print(":: Welcome to the Guess My Number App ::\n")

name = input("Please input your name:\n")

number = randint(1, 20)

print("We the computer are thinking of a number between 1 - 20")
print("You have 5 tries to guess the number before we blow you up. Choose wisely\n")

for x in range(1,6):
    guess = int(input("What is your guess number {0}?\n".format(x)))

    if guess == number:
        print("Well done {0} you get to live.\n".format(name))
        break

    elif x == 5:
        print("You guessed wrong 5 times, to the processing plant with {0}\n".format(name))

    else:
        if guess > number:
            print("Your guess is {0}, its to high.\n".format(guess))
        else:
            print("Your guess is {0}, its to low.".format(guess))
        print("You have failed to guess right, you have {0} trie(s) left.".format(5-x))


