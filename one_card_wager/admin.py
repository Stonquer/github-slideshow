from django.contrib import admin
from .models import Game, Session, Player, Seat, Table, Card, Deck

# Register your models here.
admin.site.register(Game)
admin.site.register(Session)
admin.site.register(Player)
admin.site.register(Seat)
admin.site.register(Table)
admin.site.register(Card)
admin.site.register(Deck)