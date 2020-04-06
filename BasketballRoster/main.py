print(":: Welcome to the Basketball Roster Eye ::")

roster = []

roster.append(input("\nWho is your point guard: ").title())
roster.append(input("Who is your shooting guard: ").title())
roster.append(input("Who is your small forward: ").title())
roster.append(input("Who is your power forward: ").title())
roster.append(input("Who is your center: ").title())

print("\n\tYour starting 5 for the upcoming backetball season")
print("\tPoint Guard:\t\t{0}".format(roster[0]))
print("\tShooting Guard:\t\t{0}".format(roster[1]))
print("\tSmall Forward:\t\t{0}".format(roster[2]))
print("\tPower Forward:\t\t{0}".format(roster[3]))
print("\tCenter:\t\t\t\t{0}".format(roster[4]))

print("\nOh no {0} has been injured.".format(roster[2]))
injured_player = roster[2]
roster.remove(injured_player)
print("Your roster only has {0} players now.".format(len(roster)))

roster.insert(2, input("\nWho will take {0} place? ".format(injured_player)).title())

print("\nGood luck {0} you will do great.".format(roster[2]))
print("Your roster has {0} players now.".format(len(roster)))

