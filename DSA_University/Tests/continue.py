# python code fragment to print all odd multiples of 37 in the range 501-1000
for i in range(501,1000,2):
    if i % 37 == 0:
        print(f"{i}",end=" ")
