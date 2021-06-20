"""views for shuffle"""
from Lib import secrets
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from makedecks.models import Card
from makedecks.models import Deck

def shuffle(request):
    """shuffle a deck of cards"""
    #shuffle a Deck of Cards
    cards = Card.list()
    shuffled = Deck.shuffle(cards)
    card_images = []

    for card in shuffled:
        image_dir = '<img src="/static/card_images/shuffle/'
        dex = (cards.index(card)) + 1
        strdex = str(dex)
        #card
        style = '" style="position: absolute; left: '
        pic_offset = (shuffled.index(card)) * 18
        pic_offset = str(pic_offset)
        px = 'px;">'
        output = image_dir + strdex + '.svg"' + 'alt"' + card + style + pic_offset + px
        card_images.append(output)
    myDeck = card_images
    myDeck = ''.join(myDeck)
    myDeck = mark_safe(myDeck)
    
    return render(
        request,
        'shuffle/shuffle.html',
        {
            'shuffledDeck': myDeck,
            'rawDeck': cards,
        }
    )
