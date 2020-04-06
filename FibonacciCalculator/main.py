# Print Welcome Message
print(":: Welcome to the Fibonacci Calculator App ::")

# Ask the user how many Fibonacci numbers they'd like to calculate.
fibonacci_Count = int(input("How many digits of the Fibonacci sequence would you like to compute: "))

fib_list = [1, 1]


for i in range(fibonacci_Count-1):
    fib_list.append(fib_list[len(fib_list)-1] + fib_list[len(fib_list)-2])

# Title of the Fibonacci Sequence numbers
print("\nThe first {0} numbers of the Fibonacci Sequence are: ".format(fibonacci_Count))

# Loops to print out the count of the numbers the user specified
for i in range(len(fib_list)):
    print(fib_list[i])

# Title of the Fibonacci Sequence numbers
print("\nThe Golden Ratio are: ".format(fibonacci_Count))
for i in range(len(fib_list)-1):
    print(fib_list[i+1]/fib_list[i])
