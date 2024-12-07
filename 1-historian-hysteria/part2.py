from shared import textToLists

def run(filename: str):
    (list1, list2) = textToLists(filename)

    # For each number in list1, multiply that number by the number of times it appears in list2
    # Then, add up all the products
    total = 0
    for num in list1:
        total += num * list2.count(num)
    
    # You can also do:
    # total = sum(num * list2.count(num) for num in list1)
    
    print(f"The similarity score is {total}")
