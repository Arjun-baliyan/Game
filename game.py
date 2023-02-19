import random
def game(computer,player):

    if computer=="snake":
        if player=="water":
            print("Computer win the match")
        elif player=="snake":
            print("Your both choose same - choose again")
        else:
            print("You win the match")
    elif computer=="water":
        if player=="water":
            print("You both choose same - choose again")
        elif player=="snake":
            print("You win the match")
        else:
            print("You loose the match")
    elif computer=="gun":
          if player=="water":
            print("You win the match")
          elif player=="snake":
            print("You loose the match")
          else:
            print("You both choose same - choose again")
            
randNo  = random.randint(1,3)
if randNo==1:
    computer="snake"
elif randNo==2:
    computer="water"
else:
    computer="gun"



print("Please choose from this - snake, water, gun")
player=(input("Please chooose : "))

print(("computer choose - ")+ str(computer))


game(computer,player)