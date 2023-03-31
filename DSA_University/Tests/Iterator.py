listOfNums = range(1,21)
print(type(listOfNums)) # <class 'range'>
iterator = iter(listOfNums)
"""
we could use iter() over listOfNums because
range() in Python returns a range object which is an iterable. 
You can use it to generate a series of numbers within a given range.
The most common use of range() is to iterate over a sequence of numbers 
using Python loops
"""
while True:
    try:
        val = next(iterator)
        print(val)
    except StopIteration:
        break

# the code below will end with an error, therefore "StopIterator" exception has to be caught!
while True:
    print(next(iterator))
    # if you change the body of loop here to the following:
    """
    try:
        val = next(iterator)
        print(val)
    except StopIteration:
        break
    """
    # nothing will be printed because the iterator was exhausted btw ln 3-9

