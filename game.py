import random

# Rock Paper Scissors 

#logic should be good if logic is not good then game will not work
print("wellcome to Rock, Paper, Scissors  ")
print(" coumputer trun  Rock(R) , Paper(P) , Scissors(S) :  ")

rendno = random.randint(1,3)
if rendno == 1:
    coumputer = 'R'
elif rendno == 2:
    coumputer = 'P'
elif rendno == 3:
    coumputer = 'S'


user = input("Your trun  Rock(R) , Paper(P) , Scissors(S) :  ")

def win( coumputer, user):
    #If two values are equal, declare a tie!
    if coumputer == user:
        return None
    # when coumputer will take R then!
    elif coumputer == 'R':
        if user == 'P':
            return False
        elif user == 'S':
            return True
    
    # when coumputer will take P then!
    elif coumputer == 'P':
        if user == 'R':
            return True
        elif user == 'S':
            return False

    #when coumputer will take S then!
    elif coumputer == 'S':
        if user == 'R':
            return False
        elif user == 'P':
            return True

a = win(coumputer, user)

print(f"coumputer chose {coumputer} ")
print(f"You chose {user} ")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win ")
else:
    print("You Lose ")

print("Thankyou for playing this game ")

#Code by Mr.Aakib
