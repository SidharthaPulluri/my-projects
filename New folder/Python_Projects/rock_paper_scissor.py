import random

user_score=0
computer_score=0
options=["rock",'paper','scissor','q']
while (1):
    user_input=input("type rock/paper/scissor or q to quit :").lower()
    if user_input not in options:
        print("enter valid element")
        continue
    r=random.randrange(0,3)
    computer_input=options[r]

    if user_input=="q":
        break
    
    if(user_input==computer_input):
        print("no one wins")
    elif( (computer_input=="paper" and user_input=="rock")or(computer_input=="scissor" and user_input=="paper")or(computer_input=="rock" and user_input=="scissor")):
        print("computer wins!")
        computer_score=computer_score+1 
    else:
        print("you won ")
        user_score=user_score+1 

if user_score>computer_score:
    print("you won aganist computer")
elif user_score==computer_score:
    print("its a draw")
else:
    print("computer won")


