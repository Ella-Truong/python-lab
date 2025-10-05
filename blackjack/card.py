import random

# -------------------- Card class ---------------------
class Card:
    value_map={
        'A': [1,11], '2':2, '3':3,
        '4':4, '5':5, '6':6,
        '7':7, '8':8, '9':9,
        '10':10, 'J':10, 'Q':10,'K':10
    }

    def __init__(self,val,symb):
        self.val=val
        self.symb=symb
        self.value=self.value_map[val]

    def display(self):
        # .display() -> return card as list of lines for pretty-printing
        top="+-------+"
        upper=f"|{self.symb}     {self.symb}|"
        empty="|       |"
        
        if len(self.val)==1:
            center=f"|   {self.val}   |"
        elif len(self.val)==2:
            center=f"|  {self.val}   |"
        else:
            center=f"| {self.val:^5} |"

        bottom="+-------+"

        return [top,upper,empty,center,empty,upper,bottom]
    
    def __str__(self):
        return "\n".join(self.display())
    
    def __repr__(self):
        return f"{self.val}{self.symb}"
    

# -------------------- Deck class ---------------------
class Deck:
    def __init__(self):
        self.values=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.symbols=['♠', '♥', '♦', '♣']
        self.deck=self.generate_deck()
        random.shuffle(self.deck)   #reorder 52 cards randomly

    def generate_deck(self):
        deck=[]
        for symb in self.symbols:
            for val in self.values:
                card=Card(val,symb)
                deck.append(card)
        return deck      #deck is the list of Card objects
    
    def deal_card(self):
        if not self.deck:         #check if self.deck is empty or not, not checking the self.deck exists or not as it exists when __init__() is executed
            self.regenerate()     #if not, re-create the deck again
        return self.deck.pop()    #return the last Card object in the list  --> then, the returned last Card object is passed into Hand class
    
    def regenerate(self):                #if we do deal card while the deck is empty -> crash
        self.deck=self.generate_deck()   # need to generate the new deck
        random.shuffle(self.deck)        # then shuffle before using the deck


# -------------------- Hand class ---------------------
class Hand:
    def __init__(self):
        self.cards=[]
        self.total=0
        self.aces=0

    def add_card(self,card):
        self.cards.append(card)
        if isinstance(card.value,list):   # means it's an Ace [1,11]
            self.aces+=1      #count how many ace card in hand
            self.total+=11    #first ace will start with 11 points
        else:
            self.total+=card.value
        self.adjust_for_ace()
        return self.total
    
    def adjust_for_ace(self):
        #if total > 21 and we have an Ace counted as 11, reduce total by 10
        #count that Ace as 1 instead of 11
        while self.total>21 and self.aces>0:
            self.total-=10
            self.aces-=1

    def display(self):
        if not self.cards:
            print('Hand is empty')
            return
        card_lines=[card.display() for card in self.cards]
        for i in range(len(card_lines[0])):
            print(" ".join(card[i] for card in card_lines))
    
    def is_bust(self):
        return self.total>21
    
    def is_blackjack(self):
        return self.total==21 and len(self.cards)==2

    def __str__(self):
        return f"Hand({', '.join(repr(card) for card in self.cards)}) - Total: {self.total}"
    
        




    

    

    