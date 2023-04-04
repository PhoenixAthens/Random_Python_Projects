from sys import argv
fileName = argv[1]
with open(fileName,'r+') as file:
    for ln in file:
        print(ln)

    file.seek(0)
    file.truncate()
print("DONE!!")