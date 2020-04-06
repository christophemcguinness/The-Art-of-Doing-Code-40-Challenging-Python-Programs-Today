print(':: Welcome to the Voter Registration App ::')

name = input('Please enter your name:\n'.title())
age = int(input('Please enter you age:\n'))

party_list = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']

if age >= 18:

    # prints a greeting message letting the user know they are old enough to vote
    # and give them the list of parties to join.
    print("Hello {0} you are old enough to vote.\n".format(name))
    print("Here is the list of parties you can vote for:"
          "\n{0}"
          "\n{1}"
          "\n{2}"
          "\n{3}"
          "\n{4}".format(party_list[0], party_list[1], party_list[2], party_list[3], party_list[4]))

    selected_party = input("\nPlease select the party you'd like to vote for:\n").lower()

    # based on the party the user has selected we display to the user what type of party they've joined.
    if selected_party in [x.lower() for x in party_list]:
        if selected_party in ['republican', 'democratic']:
            print("Congratulations you've joined a majority party.")
        elif selected_party in ['independent']:
            print("Congratulations you are an Independent person.")
        else:
            print("Congratulations you've joined a minority party.")
    else:
        print("The party you've selected in not in the list SORRY.")

else:
    print("You're still to young to vote. Please come back when you're 18 or older")
