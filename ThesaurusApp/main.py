from random import randint

print(":: Welcome to the Thesaurus App ::\n")

thesaurus_dict = {
    "hot": ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold": ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy": ['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad": ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

print("Here is all the words within our Thesaurus:")
for x in thesaurus_dict.keys():
    print("- {0}".format(x.title()))

valid_choice = False

users_choice = input("\nPlease select a word you'd like to know the synonym of: ").lower()

while valid_choice:
    if users_choice in thesaurus_dict.keys():
        valid_choice = True
    else:
        users_choice = input("\nYour original choice was not within our list please try again: ").lower()

print("A synonym for {0} is {1}.".format(users_choice, thesaurus_dict[users_choice][randint(0, len(users_choice) - 1)]))

see_whole_Thesaurus = input("\nWould you like to see the whole Thesaurus?(yes/no): \n").lower()

if see_whole_Thesaurus == 'yes':
    for x in thesaurus_dict.keys():
        print("\n{0} synonyms are:".format(x.title()))
        for y in thesaurus_dict[x]:
            print("- {0}".format(y.title()))
else:
    print("\nI hope you enjoyed the program. Thank you!")

