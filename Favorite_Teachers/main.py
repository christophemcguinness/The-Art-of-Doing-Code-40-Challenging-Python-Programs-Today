print(":: Welcome to the Favorite Teachers App ::")

teachers = []

teachers.append(input("\nPlease select your first favourite teacher... ").title())
teachers.append(input("Please select your second favourite teacher... ").title())
teachers.append(input("Please select your third favourite teacher... ").title())
teachers.append(input("Please select your forth favourite teacher... ").title())

print("\nYour favourite teachers ranked are {0}".format(teachers))
teachersSorted = teachers.copy()
teachersSorted.sort()
print("Your favourite teachers alphabetically are {0}".format(teachersSorted))
teachersReversed = teachers.copy()
teachersReversed.sort(reverse=True)
print("Your favourite teachers alphabetically reversed are {0}".format(teachersReversed))

print("\nYour top two favourite teachers are: {0} and {1}".format(teachers[0], teachers[1]))
print("Your next two favourite teachers are: {0} and {1}".format(teachers[2], teachers[3]))
print("Your least favourite teacher is: {0}".format(teachers[-1]))
print("You have a total of {0} teachers".format(len(teachers)))

teachers.insert(0, input("\nOpps, {0} is no longer your favourite teacher. Who is your new FAVOURITE "
                         "teacher? ".format(teachers[0])).title())

print("\nYour favourite teachers ranked are {0}".format(teachers))
teachersSorted = teachers.copy()
teachersSorted.sort()
print("Your favourite teachers alphabetically are {0}".format(teachersSorted))
teachersReversed = teachers.copy()
teachersReversed.sort(reverse=True)
print("Your favourite teachers alphabetically reversed are {0}".format(teachersReversed))

print("\nYour top two favourite teachers are: {0} and {1}".format(teachers[0], teachers[1]))
print("Your next two favourite teachers are: {0} and {1}".format(teachers[2], teachers[3]))
print("Your least favourite teacher is: {0}".format(teachers[-1]))
print("You have a total of {0} teachers".format(len(teachers)))

teachers.remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove "
                      "from your list? ").title())

print("\nYour favourite teachers ranked are {0}".format(teachers))
teachersSorted = teachers.copy()
teachersSorted.sort()
print("Your favourite teachers alphabetically are {0}".format(teachersSorted))
teachersReversed = teachers.copy()
teachersReversed.sort(reverse=True)
print("Your favourite teachers alphabetically reversed are {0}".format(teachersReversed))

print("\nYour top two favourite teachers are: {0} and {1}".format(teachers[0], teachers[1]))
print("Your next two favourite teachers are: {0} and {1}".format(teachers[2], teachers[3]))
print("Your least favourite teacher is: {0}".format(teachers[-1]))
print("You have a total of {0} teachers".format(len(teachers)))

