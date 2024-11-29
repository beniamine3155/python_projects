print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Starting the game...")
score = 0

answer = input(f"1.What does HTTP stand for in website URLs?\n")
if answer.lower() == "hypertext transfer protocol":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input(f"2.Who is known as the founder of Microsoft?\n")
if answer.lower() == "bill gates":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input(f"3.What is the name of Apple's virtual assistant?\n")
if answer.lower() == "siri":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input(f"4.What does USB stand for?\n")
if answer.lower() == "universal serial bus":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input(f"5.Which video streaming platform is owned by Google?\n")
if answer.lower() == "youtube":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input(f"6.What is the term for a program designed to harm a computer or its data?\n")
if answer.lower() == "virus":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input(f"7.What is the name of the operating system developed by Microsoft?\n")
if answer.lower() == "windows":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input(f"8.What does RAM stand for in a computer?\n")
if answer.lower() == "random access memory":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input(f"9.What does IP stand for in IP Address?\n")
if answer.lower() == "internet protocol":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input(f"10.What is the term for the main circuit board in a computer?\n")
if answer.lower() == "motherboard":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

print(f"Game Over! Your score is {score}/10")
print("You got " + str((score / 10) * 100) + "%.")