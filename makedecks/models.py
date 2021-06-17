from django.db import models

class Deck(models.Model):
    deckType = models.CharField(max_length=10)
    #like 'poker' or 'sheepshead'
    imageFormat = models.CharField(max_length=4)
    #like 'svg' or 'png'
    cardbackType = models.CharField(max_length=10)
    #like 'solid' or 'checkered'
    cardbackColor = models.CharField(max_length=10)
    #like 'red' or 'blue'
    
    def shuffle(self, cards):
        unShuffled = []
        shuffledDeck = unShuffled #placeholder
        return shuffledDeck

class Card(models.Model):
    SPADE = 0
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SUITS = (
        (SPADE, "spade"),
        (CLUB, "club"),
        (DIAMOND, "diamond"),
        (HEART, "heart")
    )
    suit = models.PositiveSmallIntegerField(choices=SUITS)
    rank = models.CharField(max_length=5)

    def list(self):
        """
        Create a list of playing cards in our database
        """
        suits = [0, 1, 2, 3]
        ranks = [
        'ace', 'two', 'three', 'four', 
        'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'jack', 'queen', 'king'
        ]
        cards = [Card(suit=suit, rank=rank) for rank in ranks for suit in suits]
        Card.objects.bulk_create(cards)



# class Deck(models.Model):
#     ranklist = [
#     'A', '2', '3', '4', 
#     '5', '6', '7', '8', 
#     '9', 'T', 'J', 'Q', 'K']

#     suitlist = ['c', 'd', 'h', 's']

#     valuelist = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#     def __init__(self):
#         self.values = models.CharField(max_length=10)
#         self.standard = models.CharField(max_length=10)

#     def create(self, i):
        
#         cardnamelist = []
#         #i = 0
    
#         for suit in self.suitlist:
#             for rank in self.ranklist:
#                 cardnamelist.append(rank + suit)
#             # cardname = self.ranklist[int(i)] + suit
#             # cardnamelist.append(cardname)
#             # i = i + .25
#         return cardnamelist

#     def CardValues(self, i):
#         cardnamelist = []
#         i = 0
#         while len(cardnamelist) < 52:
#             for suit in self.suitlist:
#                 cardname = self.ranklist[int(i)] +suit
#                 cardnamelist.append(cardname)
#                 i = i + .25
#         cardlist = dict(zip(cardnamelist, self.valuelist))
#         return cardlist
