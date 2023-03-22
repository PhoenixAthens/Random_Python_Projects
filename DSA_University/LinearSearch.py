def search(numList, element):
    index = 0
    while index < len(numList):
        if element == numList[index]:
            return index
        index += 1
    return -1


def wrapper(numList, element):
    result = search(numList, element)
    if result == -1:
        print("Value not found! ")
    else:
        print(f'Value found at {result}')


Numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8, 10, 21, 9, 102]
wrapper(Numbers, 103)
wrapper(Numbers, 1)
