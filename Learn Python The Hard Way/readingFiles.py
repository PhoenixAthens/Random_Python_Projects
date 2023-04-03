from sys import argv
file_Name = argv[1]
prompt="> "
print(f"Do you wish to read {file_Name}? Y/N")
fileOpen = open(file_Name)
response = input(prompt)
if response == "Y" or response == "y":
    print(fileOpen.read())
fileOpen.close()
print(f"Do you wish to read another file? Y/N")
response = input(prompt)
if response == "Y" or response == "y":
    print(f"Enter file name")
    file_Name=open(input(prompt))
print(f"Do you wish to read {file_Name}? Y/N")
if response == "Y" or response == "y":
    print(file_Name.read())
fileOpen.close()