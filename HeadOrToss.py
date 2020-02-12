import random
def HeadOrToss():
    randomInt = random.randint(1,2)
    if randomInt == 1:
        print ("The coin is Heads Up")
    elif randomInt==2:
        print ("The coin is Tosses Up")
def throwAgain():
    again = input("Try Again? (Y/N) \n")
    if again == 'Y' or again =='y':
        HeadOrToss()
        throwAgain()
    elif again == 'N' or again =='n':
        exit()
    else:
        print ("Please enter a correct command!")
        throwAgain()

def init():
    answer = input("Do you want to toss a coin? (Y/N) \n")
    if answer == 'Y' or answer =='y':
        HeadOrToss()
        throwAgain()
    elif answer == 'N' or answer =='n':
        exit()
    else:
        print ("Please enter a correct command!")
        init()

init()
