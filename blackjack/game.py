from players import Player
from card import Deck
import time


def hidden_card_display():
    return [
        "+-------+",
        "|░░░░░░░|",
        "|░░░░░░░|",
        "|░░░░░░░|",
        "|░░░░░░░|",
        "|░░░░░░░|",
        "+-------+"
    ]


def display_hand_with_hidden(hand, hide_first_card=False):
    if not hand.cards:
        print('Hand is empty')    
        return 
    card_lines=[]
    for i,card in enumerate(hand.cards):
        if hide_first_card and i==0:
            card_lines.append(hidden_card_display())
        else:
            card_lines.append(card.display())
    
    for i in range(len(card_lines[0])):
        print(" ".join(card[i] for card in card_lines))


def play_blackjack():
    print('--- Welcome to Blackjack ---')
    time.sleep(1)
    print('\nDealing...')
    time.sleep(1)

    deck=Deck()            #Deck() -> deck = [52 Card objects]
    player_hand=Player()   #Player() -> Hand() -> cards=[]
    dealer_hand=Player()   #Player() -> Hand() -> cards=[]

    #initial deal: 2 cards for each
    for _ in range(2):
        player_hand.hit(deck)
        dealer_hand.hit(deck)

    #show initial hands
    print("\nDealer's cards:")
    display_hand_with_hidden(dealer_hand.hand,hide_first_card=True)

    print("\nYour cards:")
    player_hand.hand.display()
    print(f"Your total: {player_hand.hand.total}")

    #check for player blackjack or bust
    if player_hand.hand.is_blackjack():
        print('Blackjack! YOU WIN 😄!')
        return
    if player_hand.hand.is_bust():
        print('Bust! You lose!')
        return

    #player's turn
    while True:
        move=input('Do you want to hit or stand? [h/s]: ').lower()
        if move=='h':
            player_hand.hit(deck)
            print("\nYour hand:")
            player_hand.hand.display()
            print(f"Your total: {player_hand.hand.total}")

            if player_hand.hand.is_bust():
                print('Bust! You lose!')
                return
            if player_hand.hand.is_blackjack():
                print('Blackjack! YOU WIN 😄!')
                break
        elif move=='s':
            break
        else:
            print("Invalid input, please type 'h' or 's'.")
    

    #dealer's turn
    print("\nDealer's cards:")
    dealer_hand.hand.display()
    print(f"Dealer total: {dealer_hand.hand.total}")

    while dealer_hand.hand.total<17:
        print('Dealer hits.')
        dealer_hand.hit(deck)
        dealer_hand.hand.display()
        print(f"Dealer total: {dealer_hand.hand.total}")

        if dealer_hand.hand.is_bust():
            print("Dealer busts! YOU WIN 😄!")
            return
    
    #final comparision
    player_total=player_hand.hand.total
    dealer_total=dealer_hand.hand.total
    
    print("\nFinal Results:")
    print(f"Your total: {player_total}")
    print(f"Dealer total: {dealer_total}")

    if dealer_total > player_total:
        print("Dealer wins 😎!")
    elif dealer_total < player_total:
        print("YOU WIN 😄!")
    else:
        print("It's a tie!")



        




