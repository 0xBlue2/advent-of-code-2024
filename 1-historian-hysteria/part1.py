from shared import textToLists

def run(filename: str):

    (list1, list2) = textToLists(filename, sort=True)

    # Find the absolute difference between the lowest values in each list, then the second-lowest values, and so on
    # Then, add up all the differences
    # |a1 - b1| + |a2 - b2| + ...
    total = 0
    for index in range(len(list1)):
        total += abs(list1[index] - list2[index])
        
    
    # You can also get the total with:
    # total = sum(abs(a - b) for (a, b) in zip(list1, list2))


    print(f"The total distance between the lists is {total}")
    return total
