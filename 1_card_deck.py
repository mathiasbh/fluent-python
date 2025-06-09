import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = ["spades", "diamonds", "clubs", "hearts"]
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        # delegates [] operator, supports splicing
        # makes deck iterable
        return self._cards[position]
    


# deck = FrenchDeck()
# from random import choice
# choice(deck)
# deck[:3]

# Card("Q", "hearts") in deck -> True
