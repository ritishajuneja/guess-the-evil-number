print("=======WELCOME To GUESS WHATT!!!======")
name=input("Enter your name: ")
print("Hi,",name,"Let's start the game.....")
print("An evil number is hiding between 1-10...")
print("Can you defeat it?")
secret=7
num=int(input("Enter a number: "))
if(num==secret):
    print("Gosh...you guessed it right....")
attempt=1
while(num!=secret):
     
     
     print("HAHA U GUESSED IT WRONG...The evil number is laughing at you...",name)
     if(num<secret):
      print("Let me give u hint...")
      print("The number u entered is less than the evil number....")
     elif(num>secret):
      print("The number u entered is higher than the evil number....")
     

     
     num=int(input("Enter a new number: "))


     attempt +=1
print("Gosh...you guessed it right....")
print("You guessed it in", attempt, "attempts")
if(attempt <= 3):
    print("DAMNN you're a genius 😭🔥")

elif(attempt <= 6):
    print("Okay okay not bad 😌")

else:
    print("That evil number bullied you 💀")
print("===== GAME OVER =====")
print("Player:", name)
print("Attempts:", attempt)
print("The evil number was:", secret)




