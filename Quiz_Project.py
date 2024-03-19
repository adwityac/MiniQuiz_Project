print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
   quit()
print("Okay! Lets play :)")
score = 0

answer = input("What does CPU stand for?")
if answer.strip().lower() == "central processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect")

answer = input("Which programming language is often used for developing Android apps?")
if answer.strip().lower() == "java":
    print("Correct!")
    score += 1

else:
    print("Incorrect")

answer = input("What is the binary equivalent of the decimal number 10?")
if answer == "1010":
    print("Correct!")
    score += 1

else:
    print("Incorrect")

answer = input("Which sorting algorithm has the best worst-case time complexity?")
if answer.strip().lower() == "merge sort":
    print("Correct!")
    score += 1

else:
    print("Incorrect")

answer = input("What is the name of the main circuit board in a computer?")
if answer.strip().lower() == "motherboard":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the term for a computer program that causes damage or allows unauthorized access?")
if answer.strip().lower() == "malware":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the term for a computer network that spans a relatively small geographical area?")
if answer.strip().lower() == "local area network" or answer.strip().lower() == "lan":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the name of the software used to translate high-level programming languages into machine code?")
if answer.strip().lower() == "compiler":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the name of the protocol that allows devices to communicate over the internet?")
if answer.strip().lower() == "tcp/ip" or answer.strip().lower() == "internet protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the term for the process of converting data into a secret code for transmission over a network?")
if answer.strip().lower() == "encryption":
    print("Correct!")
    score += 1
else:
    print("Incorrect")





print("You got" + str(score) + " questions correct!")
print("You got" + str((score / 10)*100) + "%.")
