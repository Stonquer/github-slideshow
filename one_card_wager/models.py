from django.db import models
import uuid

# class Player(Models.model):
#     First_Name = models.CharField(max_length=30)
#     Last_Name = models.CharField(max_length=30)
#     Screen_Name = models.Charfield(max_length=16)

#     def seat_assign(self):
#         """returns the seat number requested by the player"""
#         pass

# class Seat(Models.model):
    

# class Table(Models.model):


class Deck(Models.model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


# class Stack(Models.model):
#     owner = Player.Screen_Name
#     buyin = models.DecimalField(max_digits=None, decimal_places=2)
    

# class Hand(Models.model):
#     cards = 

# class Board(Models.model):
#     cards = 

# class Button(Models.model):
#     seat = 