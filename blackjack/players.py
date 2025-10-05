from card import Hand

class Player:
    def __init__(self):
        self.hand=Hand()    #player=Player() -> player.hand = <hand object>, player.hand.cards=[]

    def hit(self,deck):     #deck is passed in as parameter - an object has deal_card() method
        card=deck.deal_card()
        self.hand.add_card(card)
        return card
    
    def stand(self):
        pass

