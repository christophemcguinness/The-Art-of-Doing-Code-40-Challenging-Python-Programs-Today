def remove_smallest(numbers):


    y = numbers
    if len(numbers) == 0:
        return y , NotImplementedError("Wrong result for {0}".format(numbers))
    y = numbers
    y.remove(min(numbers))
    return y, NotImplementedError("Wrong result for {0}".format(numbers))


print(remove_smallest([1, 2, 3, 4, 5]))  # , [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
print(remove_smallest([5, 3, 2, 1, 4]))  # , [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
print(remove_smallest([1, 2, 3, 1, 1]))  # , [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
print(remove_smallest([]))  # [], "Wrong result for []"
def remove_smallest(numbers):
    raise NotImplementedError("Wrong result for {0}")
