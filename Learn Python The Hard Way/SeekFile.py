from sys import argv
script_Name,FileName=argv
print(f"Welcome to {script_Name}'s test run")
print(f"printing file {FileName}")
openedFile=open(FileName)
print("="*30)
print(openedFile.read())
print("="*30)
openedFile.seek(5) # works the way you expect, starting from 0, you reach the 5th byte using this function
print(openedFile.read())
print("="*30)