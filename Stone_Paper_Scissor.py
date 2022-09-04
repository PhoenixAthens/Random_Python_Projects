import random

listOfOptions = ["Rock", "Paper", "Scissor"]
text = "wanna play rock paper Scissor? y/n:  \n"
while True:
    value = input(f"{text}")
    if value == "y" or value == "Y":
        print("Alrighty then! I bet you can't defeat me!")

        givenAnswer = input("enter your choice Rock? Paper? Scissor?:\n")
        givenAnswer = givenAnswer.capitalize()
        if givenAnswer in listOfOptions:

            providedAnswer = random.choice(listOfOptions)

            if givenAnswer == providedAnswer:
                print("It's a tie")
                print("let's go again, i bet you can't defeat me\n")
                text = "you in then ? (y/n) \n"
            elif (givenAnswer == "Paper" and providedAnswer == "Rock") or (
                    givenAnswer == "Rock" and providedAnswer == "Scissor") or (
                    givenAnswer == "Scissor" and providedAnswer == "Paper"):
                print(" You won! ")
                print("Wanna go again?")
                text = "you in then ? (y/n) \n"

            else:
                print("told yaaa, i won!")
                print("wanna go again!")
                text = "let's do this then! Enter(y/n):\n"
        else:
            print("INVALID ENTRY")
            text = "Let's try again! (y/n) \n"
            continue
    else:
        print("It was nice meeting you! \n")
        break
