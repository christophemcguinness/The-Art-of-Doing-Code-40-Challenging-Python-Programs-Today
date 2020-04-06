def permutations(string):
    list1 = [x for x in string]
    print(list1)
    new_word = []
    newList = []

    for x in list1:
        for y in range(1, len(list1)):
            if len(new_word) > 0:
                newList.append(new_word)
                new_word = []
            for z in range(0, len(list1)):
                new_word.append(list1[z % len(list1)])

    return newList


print(sorted(permutations('a')))
