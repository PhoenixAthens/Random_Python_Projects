from sys import argv
fileName:str = argv[1]#"/Users/anmolkhanna/Downloads/To push On GIT/Python Projects/Learn Python The Hard Way/testFile.txt"
# to make the above statement work pass the file name as a string
fileContentSaver = open(fileName)
arrayOfFileContents = fileContentSaver.readline()# this reads line by line, thus code at line 8 will print first line of
# textFile.txt
text = fileContentSaver.read()
print(f"Contents: {fileContentSaver}")
print("----")
print(f"ArrayOfContents: {arrayOfFileContents}")
print("----")
print(f"Text in file: {text}")
print("----")
