print("\n:: Welcome to the Binary/Hexadecimal Converter App ::")

computeCounter = int(input("\nCompute binary and hexadecimal value up to the following decimal number: "))

dataLists = []

for nums in range(computeCounter+1):
    dataLists.append([nums, bin(nums), hex(nums)])


print(":: Generating Lists....complete! ::")

start = int(input("\nWhat decimal number would you like to start at? "))
stop = int(input("What decimal number would you like to stop at? "))

print("\nDecimal values from {0} to {1}".format(start, stop))
for nums in range(start, stop+1):
    print(dataLists[nums][0])

print("\nBinary values from {0} to {1}".format(start, stop))
for nums in range(start, stop+1):
    print(dataLists[nums][1])

print("\nHexadecimal values from {0} to {1}".format(start, stop))
for nums in range(start, stop+1):
    print(dataLists[nums][2])

# Remove item 0
dataLists.pop(0)
x = input("\nPress Enter to see all values from 1 to {0}.".format(computeCounter))

print("\nDecimal ---- Binary ---- Hexadecimal")
print("-----------------------------------------------")
for nums in dataLists:
    print('{0} --- {1} --- {2}'.format(nums[0], nums[1], nums[2]))