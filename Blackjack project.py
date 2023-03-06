
from multiprocessing import Value
from operator import truediv
from optparse import Values
from subprocess import CalledProcessError
import random
import time
PlayerIn=True
dealerin=True
    

card_score={'K':10, 'Q':10, 'J':10, '10':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'A':11}
def get_cards():
    suits=['h','c','s','d']
    card_values=['K','Q','J','10','9', '8', '7', '6', '5', '4', '3', '2', 'A']
    cards=[]
    
    for suit in suits:
        for value in card_values:
            cards.append(value+suit)
    return cards


deck = get_cards()


dealer = []
def deal(cards):
    blyat= random.randint(0, len(cards)-1)
    card= deck.pop(blyat)
    return card


dealer.append(deal(deck)) #This does the same as above
dealer.append(deal(deck))
print("Dealer's cards:",dealer)

player = []
player.append(deal(deck)) #This does the same as above
player.append(deal(deck))
print("Your cards:", player)


def get_total(cardset):
    score= 0
    aces=0
    for card in cardset:
        if card[:-1]== 'A':
            aces+=1
    for card in cardset:

        score += card_score[card[:-1]]
    if aces > 0:
        if score + 10 <= 21:
            return(score + 10)
        else:
            return(score)
    else:
        return(score)
print("Your total:", get_total(player))
print("Dealer's total:", get_total(dealer))

# dealer=[]
# hand = []
# dealt = [] 
# def game():
#     while True:

#         while get_total(player) < 21:
#             choice = input('hit[1] or stay[2]?').lower()
#             if choice == 'stay' or choice == '2':
#                 break
#             if choice == 'hit' or choice=='1':
#                 new_card = deal(deck)
#                 player.append(new_card)
#                 print(player)
#                 print("your score:", get_total(player))
#             elif get_total(player)>21:
#                 print("You are BUST!")
#             else:
#                 print("blackjack")
#                 break
#             while get_total(dealer)<17:
#                 new_card = deal(deck)
#                 dealer.append(new_card)
#                 print("Dealer Score:", get_total(dealer))
#         if get_total(dealer)==21 and get_total(player)!=21:
#             print("dealer wins!")
#             print(player)
#             print(dealer)
#         break
# print(game())

# def score():
#     player_points=0
#     dealer_points=0
#     if get_total(player)>get_total(dealer)and get_total(player)<=21:
#         player_points+=1
#     if get_total(dealer)>get_total(player)and get_total(player)<=21:
#         dealer_points+=1
#     else:
#         return player_points and dealer_points
# print(score())

for _ in range(2):
    while PlayerIn or dealerin:
        print(f"dealer has {dealer} for a total of {get_total(dealer)}")
        print(f"you have {player} for a total of {get_total(player)}")
        if PlayerIn:
            stayorhit= input("1: Stay\n2: Hit\n")
        if get_total(dealer)>16:
            dealerin=False
        else:
            dealer.append(deal(deck))
        if stayorhit=="1":
            PlayerIn= False
        else:
            player.append(deal(deck))
        if get_total(player)>=21:
            break
        elif get_total(dealer)>=21:
            break
    if get_total(player)==21:
        print(f"\nYou have {player} for a total of {get_total(player)}  and the dealer has {dealer} for a total of {get_total(dealer)}")
        print("blackjack! you win")
    elif get_total(dealer)==21:
        print(f"\n dealer has card total of {get_total(dealer)}")
        print("Dealer has Blackjack! You Lose")
    elif get_total(player)>21:
        print("oops, you went bust")
        print("dealer wins")
    elif get_total(dealer)>21:
        print("Dealer is Bust! You WIN")
# elif 21-get_total(dealer)<21-get_total(player):
#     print("dealer wins")
# elif 21-get_total(dealer)>21-get_total(player):
#     print("You win")
