end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print(end1+end2+end3+end4+end5+end6, end=' ')
print(end7+end8+end9+end10+end11+end12)
print(1,2,3,4,sep=" **Hellelujah** ")
print("Helllloo"*20)
#Output:
#HellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHellllooHelllloo
formatter = "{} {} {} {}"
#print(formatter.format("Hello","amigo",", mucho"))
print(formatter.format(1,2,3,4))
print(formatter.format(True,False,"Hello",23))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Waba",
    "Laba",
    "Dub",
    "Dub"
))
print("Hello \101")
print("Hello world, ",input())