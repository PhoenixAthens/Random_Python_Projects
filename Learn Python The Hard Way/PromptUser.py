from sys import argv
script, userName=argv
prompt=">"
print(f"Hello {userName}, Do you like chocolates? Y/N")
response = input(prompt)
if response == "Y" or response == "y":
    print("So you do like chocolates!! Good")
else:
    print("Common mannnn, who doesn't like chocolates? ")
