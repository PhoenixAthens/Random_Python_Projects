"""
consider the following Python code fragment to print
the odd numbers in the range (501, 1000) starting from
501 until it encounters an odd multiple of 37.
It prints the sequence 501, 503,..., 555.
"""
for i in range(501,1000,2):
    print(f"{i}", end=" ")
    if i%37==0: # we don't need i%2!=0 part because we are iterating an odd sequence
        break

