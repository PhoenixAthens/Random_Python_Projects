import matplotlib.pyplot as plt


def fileOP(x, name):
    xa = []
    ya = []
    with open(x, "r") as file:
        temp = file.readlines()
        for i in range(1, 25000):
            tempo = temp[i].rstrip().split(",")
            if tempo[1] == name:
                ya.append(tempo[5])
                xa.append(tempo[2])
    plt.plot(xa, ya)
    plt.show()


fileOP("SomeFile.csv", "someArgument")
# Originally I was working with a dummy csv file that had records of children with same name
# born in each year from 1900-2013, thus first argument to the method was path to that file
# on my local machine and the second argument was the name i was searching for

