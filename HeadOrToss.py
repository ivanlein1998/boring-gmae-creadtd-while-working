import random
def HeadOrToss():
    randomInt = random.randint(1,2)
    if randomInt == 1:
        print ("The coin is Heads Up")
    elif randomInt==2:
        print ("The coin is Tosses Up")
def throw():
    HeadOrToss()
    again = input("Try Again? (Y/N) \n")
    if again == 'Y' or again =='y':
        throw()
    else:
        exit()

answer = input("Do you want to toss a coin? (Y/N) \n")
if answer == 'Y' or answer =='y':
    throw()
else:
    exit()
