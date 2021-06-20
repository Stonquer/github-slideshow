"""models"""

from django.db import models
from Lib import secrets


class Card:
    class Rank:
        ranks = [
            'ace_', 'deuce_', 'trey_', 'four_',
            'five_', 'six_', 'seven_', 'eight_',
            'nine_', 'ten_', 'jack_', 'queen_', 'king_']

    class Suit:
        suits = [
            'of_clubs', 'of_diamonds',
            'of_hearts', 'of_spades'
        ]

    def list():
        cardlist = []
        ranks = Card.Rank.ranks
        suits = Card.Suit.suits
        for suit in suits:
            for rank in ranks:
                cardlist.append(rank + suit)
        return cardlist
        
class Deck:
    """What you can do with/to a Deck of Cards"""
    cards = Card.list()

    def shuffle(cards):
        """Shuffle a Deck of Cards"""
        #opdeck is the deck we'll use to shuffle
        opdeck = cards
        #initialize shuffling loop counter
        i=0
        #a number between 10-20 for the number of times to shuffle the Deck
        shuffx = secrets.randbelow(10) + 10
        #the shuffling algorithm
        while i < shuffx:
            #cut the Deck somewhere in the middle 15%
            offset = int(len(cards) * .15)
            cut = int((secrets.randbelow(8)) + offset)
            #prepare a new list to receive cards from opdeck
            shuffling = []
            i = i + 1
            #cut the deck
            deck_half1 = opdeck[0:cut]
            deck_half2 = opdeck[cut:]
            #either 1, 2, or sometimes 3 cards are chosen from each half of
            # the deck
            while len(shuffling) < len(opdeck):
                k1 = secrets.randbelow(2)
                k2 = secrets.randbelow(2)
                k3 = secrets.randbelow(10)
                k4 = secrets.randbelow(10)
                if len(deck_half1) > 0:
                    shuffling.append(deck_half1.pop())
                    if len(deck_half1) > 0:
                        if k1 > 0:
                            shuffling.append(deck_half1.pop())
                if len(deck_half2) > 0:
                    shuffling.append(deck_half2.pop())
                    if len(deck_half2) > 0:
                        if k2 > 0:
                            shuffling.append(deck_half2.pop())
                            if len(deck_half2) > 0:
                                if k4 > 7:
                                    shuffling.append(deck_half2.pop())
            #flip cards over "so no one can see them"
            shuffling.reverse()
            #clear opdeck and insert contents of shuffling deck 
            opdeck = []
            opdeck = shuffling
        #cut the cards somewhere near the middle for extra randomness
        foffset = int(len(cards) * .33)
        fcut = int((secrets.randbelow(17) * .001) + foffset)
        fCut1 = shuffling[0:fcut]
        fCut2 = shuffling[fcut:]
        shuffled = fCut2 + fCut1
        return shuffled












# class Card(models.Model):
#     """define the attributes of a Card"""
#     class Rank(models.IntegerChoices):
#         ACE = 14
#         DEUCE = 2
#         TREY = 3
#         FOUR = 4
#         FIVE = 5
#         SIX = 6
#         SEVEN = 7
#         EIGHT = 8
#         NINE = 9
#         TEN = 10
#         JACK = 11
#         QUEEN = 12
#         KING = 13

#         ranks = [
#             (ACE, 'Ace'), 
#             (DEUCE, 'Deuce'), 
#             (TREY, 'Trey'), 
#             (FOUR, 'Four'), 
#             (FIVE, 'Five'), 
#             (SIX, 'Six'), 
#             (SEVEN, 'Seven'), 
#             (EIGHT, 'Eight'), 
#             (NINE, 'Nine'), 
#             (TEN, 'Ten'), 
#             (JACK, 'Jack'), 
#             (QUEEN, 'Queen'), 
#             (KING, 'King')
#         ]

#     rank = models.IntegerField(choices=Rank.choices)

#     class Suit(models.IntegerChoices):
#         SPADE = 0
#         CLUB = 1
#         DIAMOND = 2
#         HEART = 3
#         suits = [
#             (SPADE, ' of Spades'),
#             (CLUB, ' of Clubs'),
#             (DIAMOND, ' of Diamonds'),
#             (HEART, ' of Hearts')
#         ]

#     suit = models.IntegerField(choices=Suit.choices)

#     def listCards():
#         cardlist = []
#         suits = Card.suits
#         ranks = Card.ranks
#         for suit in suits:
#             for rank in ranks:
#                 cardlist.append(rank + suit)
#         return cardlist


#         for suit in self.suitlist:
#             for rank in self.ranklist:
#                 cardnamelist.append(rank + suit)
#             # cardname = self.ranklist[int(i)] + suit
#             # cardnamelist.append(cardname)
#             # i = i + .25
#         return cardnamelist
        

# class Card(models.Model):
#     """define the attributes of a Card"""
#     SPADE = 0
#     CLUB = 1
#     DIAMOND = 2
#     HEART = 3
#     SUITS = (
#         (SPADE, "spade"),
#         (CLUB, "club"),
#         (DIAMOND, "diamond"),
#         (HEART, "heart")
#     )
#     suit = models.PositiveSmallIntegerField(choices=SUITS, default=0)
#     rank = models.CharField(max_length=5, default='ace')


#     def create_deck():
#         """
#         Create a list of playing cards in our database
#         """
#         suits = [0, 1, 2, 3]
#         ranks = [
#         'ace', 'two', 'three', 'four',
#         'five', 'six', 'seven', 'eight',
#         'nine', 'ten', 'jack', 'queen', 'king'
#         ]
#         cards = [Card(suit=suit, rank=rank) for rank in ranks for suit in suits]
#         Card.objects.bulk_create(cards)


# class Deck(models.Model):
#     """define the attributes of a Deck"""
    
#     #like 'poker' or 'sheepshead'
#     imageFormat = models.CharField(max_length=4, default='')
#     #like 'svg' or 'png'
#     cardbackType = models.CharField(max_length=10, default='')
#     #like 'solid' or 'checkered'
#     cardbackColor = models.CharField(max_length=10, default='')
#     #like 'red' or 'blue'

#     ST = 'STANDARD'
#     SH = 'SHEEPSHEAD'
#     PI = 'PINOCHLE'
#     DECKTYPE_CHOICES = [
#         (ST, 'Standard Poker Deck'),
#         (SH, 'Sheepshead Deck'),
#         (PI, 'Pinochle Deck'),
#     ]
#     deckType = models.CharField(
#         max_length=10, 
#         choices=DECKTYPE_CHOICES,
#         default='STANDARD',
#     )

#     def shuffle(deckType):
#         """shuffle the cards"""
#         cards = Card.create_deck()
#         if deckType == 'STANDARD':
#             unShuffled = cards
#             self.shuffledDeck = unShuffled #placeholder
#             return self.shuffledDeck
