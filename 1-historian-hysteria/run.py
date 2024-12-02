# find the total distance between 2 lists
# least is paired with least, 2nd least with 2nd least, and so on
# then add up the differences --> (a1 - b1) + (a2 - b2) + ...

list1 = []
list2 = []
total = 0

with open("input.txt") as input:
    for line in input:
        line = line.split() # remove whitespace and split line into 2 numbers
        list1.append(int(line[0]))
        list2.append(int(line[1]))

# sort lists so they go from least to greatest
# default order for .sort() is ascending -> 1, 2, 3 ...
list1.sort()
list2.sort()

# add up differences - one way
for index in range(len(list1)):
    total += abs(list1[index] - list2[index])


# another way
total2 = sum(abs(a-b) for a, b in zip(list1, list2))
print(total2)