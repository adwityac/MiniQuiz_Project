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




print("You got" + str(score) + " questions correct!")
print("You got" + str((score / 4)*100) + "%.")
