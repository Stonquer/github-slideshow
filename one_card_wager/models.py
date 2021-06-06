from django.db import models
import uuid

# class Player(Models.model):
#     First_Name = models.CharField(max_length=30)
#     Last_Name = models.CharField(max_length=30)
#     Screen_Name = models.Charfield(max_length=16)

#     def seat_assign(self):
#         """returns the seat number requested by the player"""
#         pass

# class Seat(models.Model):
    

# class Table(models.Model):

class Card(models.Model):
    value = models.IntegerField()
    rank = models.CharField(max_length=1)
    suit = models.CharField(max_length=1)
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

# class Deck(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     suit = 
#     rank = 
#     cards = 


# class Stack(models.Model):
#     owner = Player.Screen_Name
#     buyin = models.DecimalField(max_digits=None, decimal_places=2)
    

# class Hand(models.Model):
#     cards = 

# class Board(models.Model):
#     cards = 

# class Button(models.Model):
#     seat = 