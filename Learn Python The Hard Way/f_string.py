str1 = "So, i have been {}"
str2 = "thinking."
print(str1.format(str2))
print("Hello world, {}".format(str1).format(str2))
print(type(1))
a=str(type("Hellow"))
if a.__contains__('int'):
    print(True)
else:
    print(False)