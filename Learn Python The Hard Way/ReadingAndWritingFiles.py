from sys import argv
fileName = argv[1]
fileCapture = open(fileName)
individualLines=fileCapture.readline()
for ln in fileCapture:
    print(ln)

fileCapture.seek(0)
fileCapture.truncate() # this wouldn't work when used like this
fileCapture.close()
print("Printing!!Completed")