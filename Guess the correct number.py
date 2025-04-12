"PROJECT 2"
"GUESS THE CORRECT NUMBER"

"PLAYER-1"
import random
name1=(input("ENTER YOUR NAME PLEASE : "))
computer=random.randint(1,100)
user=-1
p1_guess=0
while(user!=computer):
    p1_guess+=1
    user=int(input(f"ENTER A NUMBER {name1} : "))
    if user>computer:
        print(f"PLEASE TRY SOME LOWER NUMBER {name1}")
    elif user<computer:
        print(f"PLEASE TRY SOME HIGHER NUMBER{name1} ")
    elif user==computer:
        print(f"YOUR GUESS IS PERFECT {name1}")
        print(f"THE NUMBER THAT COMPUTER CHOSEN IS : {computer}")

print("-------------------------------------------")
print(f"YOUR TURN IS OVER {name1}")
print("-------------------------------------------")

"PLAYER-2"
import random
name2=(input("ENTER YOUR NAME PLEASE : "))
computer=random.randint(1,100)
user=-1
p2_guess=0
while(user!=computer):
    p2_guess+=1
    user=int(input(f"ENTER A NUMBER {name2} : "))
    if user>computer:
        print(f"PLEASE TRY SOME LOWER NUMBER {name2}")
    elif user<computer:
        print(f"PLEASE TRY SOME HIGHER NUMBER {name2}")
    elif user==computer:
        print(f"YOUR GUESS IS PERFECT {name2}")
        print(f"THE NUMBER THAT COMPUTER CHOSEN IS : {computer}")

if (p1_guess>p2_guess):
    print(f"{name2} IS WINNER")
elif (p1_guess==p2_guess):
    print("IT IS A DRAW")
else:
    print(f"{name1} IS WINNER")


