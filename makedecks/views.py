"""makedecks views"""

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from . models import Card

def home(request):
    """define view for home"""
    return HttpResponse("Hello, World!")

def deckReturn(request):
    """view for looking at a deck"""
    cards = []
    cards = Card.list()
    cards = mark_safe(cards)
    return render(
    request,
    'makedecks/deckreturn.html',
    {
        "cards": cards
    }
)