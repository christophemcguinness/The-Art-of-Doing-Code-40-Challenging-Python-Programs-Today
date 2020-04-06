print("Welcome to  the Even Odd Number Sorter App")

while True:

    odd_list = []
    even_list = []

    number_string = input("\nEnter a string of numbers seperated by a comma...\n").replace(" ", "")

    if number_string[-1] == ",":
        number_string = number_string[:-1]
    elif number_string[0] == ",":
        number_string = number_string[1:]

    string_list = [int(x) for x in number_string.split(',') if x != '' and x != '0']

    print(string_list)

    print("\n----- Results Summary -----")
    for x in string_list:
        if x % 2 == 0:
            print("{0} is Even!".format(x))
            even_list.append(x)
        else:
            print("{0} is Odd!".format(x))
            odd_list.append(x)

    print("\nThe following {0} numbers(s) are Even:".format(len(even_list)))
    for x in sorted(even_list):
        print(x)

    print("\nThe following {0} number(s) are odd:".format(len(odd_list)))
    for x in sorted(odd_list):
        print(x)

    run_again = input("\nWould you like to run this app again? (y/n)..")

    if run_again.lower() != 'y':
        break

print("\nThank you for using the application. Good bye.")
