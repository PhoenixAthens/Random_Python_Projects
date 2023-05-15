from sys import argv
from os.path import exists
scriptName,from_File,to_File=argv
if exists(to_File) and exists(from_File):
    Source_Name=str(from_File).split("/").pop()
    dest_Name=str(to_File).split("/").pop()
    print(f"Copying from {Source_Name} to {dest_Name}")
    SourcePointer = open(from_File)
    contents = SourcePointer.read()
    DestinationPointer = open(to_File,"w")
    DestinationPointer.write(contents)
    print(f"Procedure completed!")
else:
    print("Invalid File Name!")