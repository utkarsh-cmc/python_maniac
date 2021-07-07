import random
randNumber = random.randint(1,100)
#print(randNumber)
guess=0
userGuess = 0
while(userGuess != randNumber ):
    userGuess = int(input("Enter your Guess: "))
    guess+=1
    if(userGuess==randNumber):
        print("You guesses it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Try guessing a lower no.") 
        else:
            print("You guessed it wrong! Try a larger no. ")
print(f"You guessed the number in {guess} guesses")

with open("highscore.txt","r") as f:
    highscore=int(f.read())

if(guess<highscore):
    print("You have broke the highscore !!")
    with open("highscore.txt","w") as f:
        f.write(str(guess))