import cmath

# Print title and explanation of the application
print("\n:: Welcome to the Quadratic Equation Solver App ::")
print("\n\nA Quadratic Equation is of the form ax^2 + bx + c = 0")
print("Your solution can include real numbers or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary number.")


# How many equations you'd like to solve
count = int(input("\nHow many equations would you like to solve today? "))

# Loop through the count of the equations you'd like to solve talking the 3 coefficients
# Can be both real or imaginary numbers.
for num in range(count):
    print("\nSolving equation #{0}".format(num+1))
    print("------------------------------------------")
    a = float(input("Please enter the value for a (coefficient of x^2): "))
    b = float(input("Please enter the value for a (coefficient of x): "))
    c = float(input("Please enter the value for a (coefficient): "))

    # within the loop print the solution to the equations.
    print("The solution to {0}x^2 + {1}x + {2} is: ".format(a, b, c))
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    print("x1 = {0}".format(sol1))
    print("x2 = {0}".format(sol2))

# Goodbye message.
print("Thank you for using the Quadratic Equation Solver App. Goodbye")




