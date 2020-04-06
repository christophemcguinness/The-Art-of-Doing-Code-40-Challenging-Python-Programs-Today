print(":: Welcome to the Factor Generator App ::")

while True:
    factor_number = int(input("\nPlease input a number you'd like to find the factor of..."
                              "\n"))
    min_numbers = []
    max_numbers = []

    for x in range(1, factor_number+1):
        if factor_number % x == 0:
            min_numbers.append(x)
            max_numbers.append(int(factor_number / x))

    print("Factors of {0}:".format(factor_number))
    for x in sorted(set(min_numbers + max_numbers)):
        print(x)

    print("\nIn summary:")
    for x, y in zip(min_numbers, max_numbers):
        print("{0} * {1} = {2}".format(x, y, factor_number))

    go_again = input("\nWould you like to try this again with a new number? (y/n):\n")

    if go_again.lower() != 'y':
        break
