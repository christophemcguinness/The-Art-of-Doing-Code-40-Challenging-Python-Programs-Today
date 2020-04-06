print("::Welcome to the Yes or No Polling App ::")

issue = input("\nWhat is the issue you'd like voters to vote on today? ")

voters_numbers = int(input("How many voters would you like to vote today? "))

poll_password = input("What password would you like to in order to view the poll results? ")

yes_votes = 0
no_votes = 0

results = {}

for x in range(voters_numbers):
    fullname = input("\nHello Voter please input your full name... ")

    if fullname in results:
        print("\nSorry {0} you've already voted, you can't vote again".format(fullname))
    else:
        print("\n{0}".format(issue))
        choice = input("What is your decision? Yes or No? ")

        if choice.lower() == "yes" or choice.lower() == 'y':
            yes_votes += 1
            choice = "yes"
        elif choice.lower() == "no" or choice.lower() == 'n':
            no_votes += 1
            choice = "no"
        else:
            print("\nYour vote will be recorded but we can increase the counts due to you not giving a"
                  " definite answer. ")

        results[fullname] = choice

        print("Thank you for voting.")

print("\nThe Total number of voters where {0}".format(voters_numbers))
print("Full names: ")
for x in results.keys():
    print(x)

print("\nThe vote resutls are {0} for yes and {1} for no.".format(yes_votes, no_votes))

print("\nThe vote was about '{0}'".format(issue))

if yes_votes == no_votes:
    print("The results are in and its a tie.")
elif yes_votes > no_votes:
    print("The yes's have it.")
else:
    print("The no's have it.")

users_password = input("\nPlease input the password in order to see the results of the people... ")

if users_password == poll_password:
    print("\nFull Names and Their choices:")
    for x in results.keys():
        print("{0} voted for {1}".format(x.title(), results[x].title()))
else:
    print("\nSorry the password you've input does not match so you can't view the results.")

print("\n\nThanks for using this program.")
