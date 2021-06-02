from django.http import HttpResponse
from django.shortcuts import render
from Lib import secrets
from django.utils.safestring import mark_safe


def one_card_intro(request):
    return render(
        request,
        'one_card_intro/one_card_intro.html',
        {
#            'myCard': myCard,
        }
    ) 

def one_card_wager(request):

    un_shuffled = [
    'Ac', 'As', 'Ah', 'Ad', 'Kc', 'Ks', 'Kh', 'Kd', 'Qc', 'Qs', 'Qh', 'Qd', 
    'Jc', 'Js', 'Jh', 'Jd', 'Tc', 'Ts', 'Th', 'Td', '9c', '9s', '9h', '9d', 
    '8c', '8s', '8h', '8d', '7c', '7s', '7h', '7d', '6c', '6s', '6h', '6d', 
    '5c', '5s', '5h', '5d', '4c', '4s', '4h', '4d', '3c', '3s', '3h', '3d', 
    '2c', '2s', '2h', '2d']

    opdeck = un_shuffled
    i = 0
    shuffX = secrets.randbelow(10) + 10
    Ac_index = []

    while i < shuffX:
        offset = int(len(un_shuffled) * .33)
        cut = int((secrets.randbelow(17)) + offset) 
        shuffling = []
        i = i + 1
        deck_half1 = opdeck[0:cut]
        deck_half2 = opdeck[cut:]

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
                        if len(deck_half1) > 0:
                            if k3 > 7:
                                shuffling.append(deck_half1.pop())

            if len(deck_half2) > 0:
                shuffling.append(deck_half2.pop())
                if len(deck_half2) > 0:
                    if k2 > 0:
                        shuffling.append(deck_half2.pop())
                        if len(deck_half2) > 0:
                            if k4 > 7:
                                shuffling.append(deck_half2.pop())

        shuffling.reverse()
        opdeck = []
        opdeck = shuffling
        Ac_report = shuffling.index('Ac')
        Ac_index.append(Ac_report)

    foffset = int(len(un_shuffled) * .33)
    fcut = int((secrets.randbelow(17) * .001) + foffset)
    fCut1 = shuffling[0:fcut]
    fCut2 = shuffling[fcut:]
    shuffled = fCut2 + fCut1
    Ac_report = shuffled.index('Ac')
    Ac_index.append(Ac_report)

    card_images = []
    for card in shuffled:
        image_dir = '<img src="/static/card_images/shuffle/'
        style = 'style="position: absolute; left: '
        dex = un_shuffled.index(card) + 1
        strdex = str(dex)
        pic_offset = str(shuffled.index(card) * 12)
        output = image_dir + strdex + '.png"' + ' alt="' + card + '" ' + style + pic_offset + 'px";>'
        card_images.append(output)

    shuffled = card_images

    myCard = shuffled[0]

    myDeck = (' '.join(shuffled))

    myDeck = mark_safe(myDeck)
    myCard = mark_safe(myCard)

    return render(
        request,
        'one_card_wager/one_card_wager.html',
        {
            'myCard': myCard,
        }
    ) 

def check(request):
    return render(
        request,
        'one_card_wager/check.html',
        {
            'myCard': myCard,
        }
    )
