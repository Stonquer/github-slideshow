from django.db import models
import uuid

class Player(models.Model):
    acctNo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Screen_Name = models.CharField(max_length=16)


#    def __init__(self, First_Name, Last_Name, Screen_Name, userID):
#        self.First_Name = First_Name
#        self.Last_Name = Last_Name
#        self.Screen_Name = Screen_Name
#        self.userID = userID

class Seat(models.Model):
    table = models.IntegerField()
    number = models.IntegerField()
    taken = models.BooleanField()
    occupant = models.ForeignKey(Player.Screen_Name, on_delete=models.SET_NULL, null=True)

#    def __init__(self, table, number, taken, occupant):
#        self.table = table
#        self.number = number
#        self.taken = taken
#        self.occupant = occupant


class Table(models.Model):
    number = models.IntegerField(primary_key=True)
    maxPlayers = models.IntegerField()
    ONECARDWAGER = 'OCWG'
    NLTEXHOLD = 'NLHE'
    PLOMAHA = 'PLO'
    DOMAHA = 'DOMA'
    GAMESELECT_CHOICES = [
        (ONECARDWAGER, 'One Card Wager'),
        (NLTEXHOLD, 'No Limit Texas Hold Em'),
        (PLOMAHA, 'Pot Limit Omaha'),
        (DOMAHA, 'Domaha'),
    ]
    gameselect = models.CharField(
        max_length=4,
        choices=GAMESELECT_CHOICES,
        default=ONECARDWAGER,
    )

class Card(models.Model):
    value = models.IntegerField()
    rank = models.CharField(max_length=1)
    suit = models.CharField(max_length=1)
    name = models.CharField(max_length=2)
    deck = models.ForeignKey('deck.id', on_delete=models.SET_NULL, null=True)
    backImage = models.CharField(max_length=100)
    faceImage = models.CharField(max_length=100)

    def __init__(self, name, value, deck):
        self.name = self.rank + self.suit
        self.value = value
        self.deck = deck

    def CardImage(card):

    #assign card image to player's card
    image_dir = '<img src="/static/card_images/shuffle/'
    dex = un_shuffled.index(myCard) + 1
    strdex = str(dex)
    output = image_dir + strdex + '.png"' + ' alt="' + myCard + '">'
    myCardImage = output

#    """String for representing a Card"""
#    def __str__(self):
#        return self.name

# class Deck(models.Model):
#     cards = []
#     brand = models.CharField(max_length=20)
#     backpattern = models.CharField(max_length=20)
#     decktype = models.Charfield(max_length=20)

# #     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# #     suit = 
# #     rank = 
# #     cards = 


# class Stack(models.Model):
#     owner = Player.Screen_Name
#     buyin = models.DecimalField(max_digits=None, decimal_places=2)
    

#class Hand(models.Model):
#
#    firstCard = deck.pop(0)
#    secondCard = deck.pop(0)
#     cards = cards[(firstCard, secondCard)]

# class Board(models.Model):
#     cards = 

# class Button(models.Model):
#     seat = 