print(" Welcome to my Quiz!")
answer=input("do you want to play the game :")
c=0
answer.lower()
if answer!="yes":
    quit()
print("Lets Get Started!")
answer=input("whats capital of India :")
answer.lower()
if answer=="delhi":
    print("yay! that's correct")
    c=c+1
else:
    print("not correct")

answer=input("whats capital of USA")
answer.lower()
if answer=="washington dc":
    print("yay! that's correct")
    c=c+1
else:
    print("not correct")

answer=input("whats the capital of telangana:")
answer.lower()
if answer=="hyderabad":
    print("yay! that's correct")
    c=c+1
else:
    print("not correct")

answer=input("whats GPU stands for:")
answer.lower()
if answer=="graphics processing unit":
    print("yay! that's correct")
    c=c+1
else:
    print("not correct")

print("you got" ,c,"Questions correct",c)