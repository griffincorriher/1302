from random import shuffle as rshuffle

class Card:
    _SUITS = ['s', 'h', 'c', 'd']
    _SUIT_NAMES = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    _RANKS = list(range(1,14))
    _RANK_NAMES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
        'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    def __init__(self, suit, rank):
        """
        suit should be one of the following strings:
        h (for hearts), s (for spades), c (for clubs), d (for diamonds)

        rank should be an integer 1-13, inclusive
        1 = Ace, 11 = Jack, 12 = Queen, 13 = King
        """
        # The parameters suit and rank are LOCAL variables
        # We will save them as instance variables
        if suit in self._SUITS:
            self.suit = suit
        else:
            raise ValueError("suit must be s h c or d")
        if rank in self._RANKS:
            self.rank = rank
        else:
            raise ValueError("rank must be integer 1-13, inclusive")
        
    def __str__(self):
        rank_name = self._RANK_NAMES[self._RANKS.index(self.rank)]
        suit_name = self._SUIT_NAMES[self._SUITS.index(self.suit)]
        return rank_name + " of " + suit_name
    
    def __eq__(self, other):
        """ Returns True if self == other, that is, that the rank and suit 
        are the same.  Returns False otherwise. """
        return self.suit == other.suit and self.rank == other.rank
    
    def __lt__(self, other):
        """ Order defined on cards is: check ranks first.
        If ranks are the same, check suit.  Club < Diamonds < Hearts < Spades """
        if self.rank < other.rank:
            return True
        elif self.rank > other.rank:
            return False
        else:
            suit_order = ['c','d','h','s']
            return suit_order.index(self.suit) < suit_order.index(other.suit)

class Deck:
    def __init__(self):
        """ Initalizes a full standard 52 card deck """
        self.deck = []
        for suit in Card._SUITS:
            for rank in Card._RANKS:
                self.deck.append(Card(suit, rank))
    
    def shuffle(self):
        """ Shuffle the deck randomly """
        rshuffle(self.deck)

    def deal(self):
        """ Deals (returns) one card from the deck """
        return self.deck.pop()
    
    def size(self):
        """ Returns number of cards currently in deck """
        return len(self.deck)

        
class Hand:
    def __init__(self, cards=[]):
        """ Creates Hand from given cards.  If no cards are given, creates 
        empty hand."""
        self.cards = []
        for card in cards:
            if type(card) == Card:
                self.cards.append(card)
            else:
                raise TypeError("Hand must contain Card objects")

    def add(self, cardtoadd):
        """ Adds cardtoadd to bottom of hand. """
        if type(cardtoadd) == Card:
            self.cards.append(cardtoadd)
        else:
            raise TypeError("Hand must contain Card objects")

    def remove(self, cardtoremove):
        """ Removes cardtoremove from Hand if it exists. If not, raises
        ValueError. """
        self.cards.remove(cardtoremove)

    def discard_top(self):
        """ Removes and returns top card from Hand. """
        return self.cards.pop(0)

    def discard_index(self, start, stop=0):
        """ Discards index start through index stop (inclusive) from current 
        hand.  Returns discarded card(s) as a hand.
        If you only want to discard one card, use start parameter only. """
        if stop < start:
            raise ValueError("stop value must be > start value")
        if stop == 0:
            discard_hand = Hand()
            discard_hand.add(self.cards.pop(start))
            return discard_hand
        else:
            discard_hand = Hand()
            for i in range(start,stop+1):
                discard_hand.add(self.cards.pop(start))
            return discard_hand

    def __str__(self):
        """ Prints all cards in Hand. """
        answer = ''
        for card in self.cards:
            answer += str(card) + '\n'
        return answer[:-1]

    def get_ranks(self):
        """ Returns list of ints corresponding to ranks of cards in self """
        answer = []
        for card in self.cards:
            answer.append(card.rank)
        return answer
    
    def SortByRank(self):
        """ Sorts Cards in hand according to rank (lowest first) """
        self.cards.sort()
    
    def PrintWithIndexes(self):
        """ Prints name of all cards in Hand, with an index label for each """
        for i, C in self.cards:
            print(i, " ", C)
    
    def absorb(self,other):
        """ Adds all cards in other to current hand, but without removing those 
        cards from the other hand """
        for C in other.cards:
            self.add(C)
        

    
    





"""
x = Card('c', 7)
print(x)
y = Card('h', 1)
print(y)
z = Card('d', 8)
print(type(z) == Card)

try:
    a = Card("C", 7)
except Exception as E:
    print(E)

try:
    b = Card('h', 15)
except Exception as E:
    print(E)

try:
    c = Card('hearts', 4)
except Exception as E:
    print(E)
"""
