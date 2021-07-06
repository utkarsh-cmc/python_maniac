#stone paper scissor game
import random 
def gameWin(comp , user):
    if comp==user:
        return None
    elif comp=='s':
        if user=='sc':
            return False 
        elif user=='p': 
            return True  
    elif comp=='p':
        if user=='s':
            return False 
        elif user=='sc': 
            return True          
    elif comp=='sc':
        if user=='p':
            return False 
        elif user=='s': 
            return True  


print ("Welcome to the 'Stone Paper Scissors' game :")
print("You will play against a computer")
print("####\t Your Choices are Stone(s) , Paper(p) , Scissors(sc) \t####")

randno=random.randint(1,3)
if randno==1:
   comp='s'
if randno==2:
   comp='p'
else :
   comp='sc'

userI=input("Enter your Choice : \n")
result=gameWin(comp,userI)

print(f"computer chose {comp}")
print(f"user chose {userI}")

if result==None:
    print("Game Tied")
elif result:
    print("You Won!\n :)")
else:
    print("You Loose \n:(")        