import datetime as dt

print("\n:: Welcome to the Grocery List App ::")

dateTime = dt.datetime.now()

print("\nThe current time is: {0}:{1} and the current date is: {2}/{3}/{4}".format(dateTime.hour, dateTime.minute, dateTime.day, dateTime.month, dateTime.year))
groceryList = ["Apples", "Oranges"]

print("\nYour current list: {0}".format(groceryList))
print("Please add 3 extra items to your shopping list")
groceryList.append(input("Please add the first extra item... ").title())

print("\nYour current list: {0}".format(groceryList))
groceryList.append(input("Please add the second extra item... ").title())

print("\nYour current list: {0}".format(groceryList))
groceryList.append(input("Please add the third extra item... ").title())

groceryList.sort()

print("Your sorted shopping list looks like this: {0}".format(groceryList))


print("\nYour current list: {0}".format(groceryList))
groceryList.remove(input("Please input the first item you'd like to check off the list... ").title())
print("\nYour current list: {0}".format(groceryList))
groceryList.remove(input("Please input the second item you'd like to check off the list... ").title())
print("\nYour current list: {0}".format(groceryList))
groceryList.remove(input("Please input the third item you'd like to check off the list... ").title())

print("\nYour current list: {0}".format(groceryList))
groceryList.insert(0, input("\nThe item {0} is no longer available in the shop, please input an alternative... ".format(groceryList.pop())).title())

# groceryList.remove(groceryList[0])

print("\nYour current list: {0}".format(groceryList))
groceryList.remove(input("Please input the third item you'd like to check off the list... ").title())

print("\nYour current list: {0}".format(groceryList))
groceryList.remove(input("Please input the forth item you'd like to check off the list... ").title())
