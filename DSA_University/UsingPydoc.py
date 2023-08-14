def linSearch(element:int, listOfElems:[int])->int:
    """ Search for element in listOfElems
    :param element: the element being searched for
    :param listOfElems: list of elements being inspected
    :return:
    the index at which the element is found within listOfElements,
    -1 otherwise

    """
    length = len(listOfElems)
    for i in range(0,length):
        if listOfElems[i] == element:
            return i
    return -1

help(linSearch)

# Compiler Optimization
# inline functions
def PiTwice_1(upperLimit:int):
    alist = []
    pi = 3.14
    for i in range(upperLimit):
        alist.append(2*i*pi) # this has to be declared first
    print(alist)
PiTwice_1(20)

# optimized PiTwice_1
def PiTwice_2(upperLimit:int):
    alist:[float] = [ ]
    piTwice = 3.14*2
    for i in range(upperLimit):
        alist.append(piTwice*i)
    print(alist)
PiTwice_2(20)

