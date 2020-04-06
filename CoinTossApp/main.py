from random import randint

print(':: Welcome to the Coin Toss App ::\n')

turns = int(input("Please input the number of times you'd like to toss the coin?\n"))

see_results = input('Would you like to see the individual coin flips or not?\n').lower()

see_results = see_results[0]

print(see_results)

heads_count = 0
tails_count = 0

print('Flipping!!\n')
for x in range(turns):
    if see_results == 'y':
        if randint(0, 1) == 0:
            heads_count += 1
            print('Turn {0} is Heads'.format(x + 1))
        else:
            tails_count += 1
            print('Turn {0} is Tails'.format(x + 1))
        if heads_count == tails_count:
            print('Currently counts for heads and tails are both the same.')

    else:
        if randint(0, 1) == 0:
            heads_count += 1
        else:
            tails_count += 1

print('\nResults of flipping a coin {0} times')

print('Side \tCount \t\tPercentage')
print('Heads: \t{0}/{1} \t{2}%'.format(heads_count, turns, round((100 / turns) * heads_count, 2)))
print('Tails: \t{0}/{1} \t{2}%'.format(tails_count, turns, round((100 / turns) * tails_count, 2)))

