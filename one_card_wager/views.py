from django.http import HttpResponse
from django.shortcuts import render
from Lib import secrets
from django.utils.safestring import mark_safe
#from .models import Card

def one_card_intro(request):
    """A button to shuffle a deck and start playing the game 'One Card Wager'"""

    #My Card and Computer Card session init
    myCard = request.session.get('myCard')
    myCardValue = request.session.get('myCardValue')
    myCardImage = request.session.get('myCardImage')
    compCard = request.session.get('compCard')
    compCardValue = request.session.get('compCardValue')
    compCardImage = request.session.get('compCardImage')
    Ac_index = request.session.get('Ac_index')

    un_shuffled = [
    'Ac', 'As', 'Ah', 'Ad', 'Kc', 'Ks', 'Kh', 'Kd', 'Qc', 'Qs', 'Qh', 'Qd', 
    'Jc', 'Js', 'Jh', 'Jd', 'Tc', 'Ts', 'Th', 'Td', '9c', '9s', '9h', '9d', 
    '8c', '8s', '8h', '8d', '7c', '7s', '7h', '7d', '6c', '6s', '6h', '6d', 
    '5c', '5s', '5h', '5d', '4c', '4s', '4h', '4d', '3c', '3s', '3h', '3d', 
    '2c', '2s', '2h', '2d']

    rankKey = [
    14, 14, 14, 14, 13, 13, 13, 13, 12, 12, 12, 12, 
    11, 11, 11, 11, 10, 10, 10, 10, 9, 9, 9, 9, 
    8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 
    5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 
    2, 2, 2, 2]

    #copy un_shuffled to opdeck
    opdeck = un_shuffled

    #initialize counter for shuffX
    i = 0
    
    #pick a number between 10-20 for shuffX
    shuffX = secrets.randbelow(10) + 10

    #debug parameter to track Ace of Clubs
    Ac_index = []

    #The shuffling algorithm
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

    #cut the cards somwhere near the middle for extra randomness
    foffset = int(len(un_shuffled) * .33)
    fcut = int((secrets.randbelow(17) * .001) + foffset)
    fCut1 = shuffling[0:fcut]
    fCut2 = shuffling[fcut:]
    shuffled = fCut2 + fCut1
    Ac_report = shuffled.index('Ac')
    Ac_index.append(Ac_report)

    #Deal 1st card to player, 2nd card to computer    
    myCard = shuffled[0]
    myCardIndex = un_shuffled.index(myCard)
    myCardValue = rankKey[myCardIndex]
    compCard = shuffled[1]
    compCardIndex = un_shuffled.index(compCard)
    compCardValue = rankKey[compCardIndex]

    #assign card images
    image_dir = '<img src="/static/card_images/shuffle/'
    dex = un_shuffled.index(myCard) + 1
    strdex = str(dex)
    output = image_dir + strdex + '.png"' + ' alt="' + myCard + '">'
    myCardImage = output

    image_dir = '<img src="/static/card_images/shuffle/'
    dex = un_shuffled.index(compCard) + 1
    strdex = str(dex)
    output = image_dir + strdex + '.png"' + ' alt="' + compCard + '">'
    compCardImage = output

    #session counter
    counter = request.session.get('counter', 0)
    counter += 1
    request.session['counter'] = counter

    #take away quote marks for html insertion
    myCardImage = mark_safe(myCardImage)
    compCardImage = mark_safe(compCardImage)

    #store My Card, Computer's Card, images, and ranks to session
    request.session['myCard'] = myCard
    request.session['myCardValue'] = myCardValue
    request.session['myCardImage'] = myCardImage
    request.session['compCard'] = compCard
    request.session['compCardValue'] = compCardValue
    request.session['compCardImage'] = compCardImage
    request.session['Ac_index'] = Ac_index

    return render(
        request, 'one_card_wager/one_card_intro.html') 


def one_card_wager(request):
    """Get session data from 'intro' page. HTML file gives player 
    two options: check or bet"""

    #My Card and Computer Card session init
    myCard = request.session.get('myCard')
    myCardValue = request.session.get('myCardValue')
    myCardImage = request.session.get('myCardImage')
    compCard = request.session.get('compCard')
    compCardValue = request.session.get('compCardValue')
    compCardImage = request.session.get('compCardImage')
    Ac_index = request.session.get('Ac_index')
    counter = request.session.get('counter', 0)

    #take away quote marks for html insertion
    myCardImage = mark_safe(myCardImage)
    compCardImage = mark_safe(compCardImage)

    #store My Card, Computer Card, images, and ranks to session
    request.session['myCard'] = myCard
    request.session['myCardValue'] = myCardValue
    request.session['myCardImage'] = myCardImage
    request.session['compCard'] = compCard
    request.session['compCardValue'] = compCardValue
    request.session['compCardImage'] = compCardImage
    request.session['Ac_index'] = Ac_index


    return render(
        request,
        'one_card_wager/one_card_wager.html',
        {
            'myCardImage': myCardImage,
            'compCardImage': compCardImage,
            'counter': counter,
            'myCardValue': myCardValue,
            'compCardValue': compCardValue,
            'Ac_index': Ac_index,
            'myCard': myCard,
            'compCard': compCard,
        }
    )


def check(request):
    """one_card_wager/game/check/ : When player checks"""

    #get variables from session
    counter = request.session.get('counter')
    request.session['counter'] = counter
    myCard = request.session.get('myCard')
    myCardImage = request.session.get('myCardImage')
    myCardValue = request.session.get('myCardValue')
    compCard = request.session.get('compCard')
    compCardImage = request.session.get('compCardImage')
    compCardValue = request.session.get('compCardValue')
    Ac_index = request.session.get('Ac_index')
    compAction = request.session.get('compAction')
    result = request.session.get('result')

    myCardImage = mark_safe(myCardImage)
    compCardImage = mark_safe(compCardImage)

    k100 = secrets.randbelow(100)
    if compCardValue == 14:
        compAction = 'bet'
    elif compCardValue >= 10:
        if k100 > 25:
            compAction = 'bet'
    else:
        compAction = None

    if compAction == 'bet':

        #store variables to session
        request.session['myCard'] = myCard
        request.session['myCardValue'] = myCardValue
        request.session['myCardImage'] = myCardImage
        request.session['compCard'] = compCard
        request.session['compCardValue'] = compCardValue
        request.session['compCardImage'] = compCardImage
        request.session['Ac_index'] = Ac_index
        request.session['compAction'] = compAction
        request.session['k100'] = k100
#        request.session['result'] = result

        return render(
            request,
            'one_card_wager/check.html',
            {
            'myCardImage': myCardImage,
            'compCardImage': compCardImage,
            'counter': counter,
            'myCardValue': myCardValue,
            'compCardValue': compCardValue,
            'Ac_index': Ac_index,
            'myCard': myCard,
            'compCard': compCard,
            'compAction': compAction,
            'k100': k100,
#            'result': result,
            
            }
        )

    else:
        if compCardValue <= 7:
            compAction = None
        if myCardValue > compCardValue:
            result = "You Won the Showdown!"
        if myCardValue < compCardValue:
            result = "You Lost the Showdown!"
        else:
            if myCardValue == compCardValue:
                result = "It's a Tie!"

    
    #store variables to session
    request.session['myCard'] = myCard
    request.session['myCardValue'] = myCardValue
    request.session['myCardImage'] = myCardImage
    request.session['compCard'] = compCard
    request.session['compCardValue'] = compCardValue
    request.session['compCardImage'] = compCardImage
    request.session['Ac_index'] = Ac_index
    request.session['compAction'] = compAction
    request.session['k100'] = k100
    request.session['result'] = result

    return render(
        request,
        'one_card_wager/check.html',
        {
            'myCardImage': myCardImage,
            'compCardImage': compCardImage,
            'counter': counter,
            'myCardValue': myCardValue,
            'compCardValue': compCardValue,
            'Ac_index': Ac_index,
            'myCard': myCard,
            'compCard': compCard,
            'compAction': compAction,
            'k100': k100,
            'result': result,
        }
    )

def showdown(request):
    """one_card_wager/game/check/ : When player calls"""
    #get variables from session
    counter = request.session.get('counter')
    request.session['counter'] = counter
    myCard = request.session.get('myCard')
    myCardImage = request.session.get('myCardImage')
    myCardValue = request.session.get('myCardValue')
    compCard = request.session.get('compCard')
    compCardImage = request.session.get('compCardImage')
    compCardValue = request.session.get('compCardValue')
    Ac_index = request.session.get('Ac_index')
    compAction = request.session.get('compAction')
    k100 = request.session.get('k100')
    

    myCardImage = mark_safe(myCardImage)
    compCardImage = mark_safe(compCardImage)

    if myCardValue == compCardValue:
        result = "It's a Tie!"
    elif myCardValue > compCardValue:
        result = "You Won the Showdown!"
    elif myCardValue < compCardValue:
        result = "You Lost the Showdown!"

    #store variables to session
    request.session['myCard'] = myCard
    request.session['myCardValue'] = myCardValue
    request.session['myCardImage'] = myCardImage
    request.session['compCard'] = compCard
    request.session['compCardValue'] = compCardValue
    request.session['compCardImage'] = compCardImage
    request.session['Ac_index'] = Ac_index
    request.session['compAction'] = compAction
    request.session['k100'] = k100
    request.session['result'] = result

    return render(
        request,
        'one_card_wager/showdown.html',
        {
            'myCardImage': myCardImage,
            'compCardImage': compCardImage,
            'counter': counter,
            'myCardValue': myCardValue,
            'compCardValue': compCardValue,
            'Ac_index': Ac_index,
            'myCard': myCard,
            'compCard': compCard,
            'compAction': compAction,
            'k100': k100,
            'result': result,
        }
    )