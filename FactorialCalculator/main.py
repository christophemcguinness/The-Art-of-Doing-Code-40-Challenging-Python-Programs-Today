import math

# Print the welcome message
print("\n:: Welcome to the Factorial Calculator App ::")

# Gets the number the user would like the calculate the factorial of.
factorial_num = int(input("\nWhat number would you like to compute the factorial of? "))
equation = ""

for i in range(factorial_num):
    equation = equation + "{0}*".format(i + 1)

print("{0}! = {1}".format(factorial_num, equation[:-1]))

# Print the results of the math library
lib_Results = math.factorial(factorial_num)
print("\nHere is the results from the maths Library:\nThe factual of {0} is {1}".format(factorial_num, lib_Results))

manual_Results = 1
# Print the manual output
for i in range(factorial_num):
    manual_Results = manual_Results * (i + 1)

print("\nHere is the results from the manual calculation:\nThe factual of {0} is {1}!".format(factorial_num,
                                                                                              manual_Results))
# Print the final message
print("\nIt is shown twice that {0}! = {1} (with excitement)".format(factorial_num, manual_Results))
