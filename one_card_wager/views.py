from django.http import HttpResponse
from django.shortcuts import render
from Lib import secrets
from django.utils.safestring import mark_safe
from makedecks.models import Deck

#global constants (or what I'm calling "global constants")
cardBackImage = mark_safe('<img src="/static/card_images/shuffle/cardback.png" alt="cardBack">')
ante = 1
betsize = 2

def signin(request):
    """sign-in to the site"""
    pass

def acctDetails(request):
    pass

def gameSelect(request):
    
        return render(
        request, 
        'one_card_wager/gameSelect.html',

        {

        }
    ) 
1
def one_card_intro(request):
    """A button to shuffle a deck and start playing the game 'One Card Wager'"""

    #Cards, stack, and session init
    myCard = request.session.get('myCard')
    myCardValue = request.session.get('myCardValue')
    myCardImage = request.session.get('myCardImage')
    compCard = request.session.get('compCard')
    compCardValue = request.session.get('compCardValue')
    compCardImage = request.session.get('compCardImage')
    Ac_index = request.session.get('Ac_index')

    compStack = request.session.get('compStack', 100)
    playerStack = request.session.get('playerStack', 100)

    un_shuffled = Deck.create(Deck, i=0)
#    un_shuffled = [
#    'Ac', 'As', 'Ah', 'Ad', 'Kc', 'Ks', 'Kh', 'Kd', 'Qc', 'Qs', 'Qh', 'Qd', 
#    'Jc', 'Js', 'Jh', 'Jd', 'Tc', 'Ts', 'Th', 'Td', '9c', '9s', '9h', '9d', 
#    '8c', '8s', '8h', '8d', '7c', '7s', '7h', '7d', '6c', '6s', '6h', '6d', 
#    '5c', '5s', '5h', '5d', '4c', '4s', '4h', '4d', '3c', '3s', '3h', '3d', 
#    '2c', '2s', '2h', '2d']

    rankKey = [
    14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,]

#    14, 14, 14, 14, 13, 13, 13, 13, 12, 12, 12, 12, 
#    11, 11, 11, 11, 10, 10, 10, 10, 9, 9, 9, 9, 
#    8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 
#    5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 
#    2, 2, 2, 2]

    #copy the un-shuffled deck to an operational deck
    opdeck = un_shuffled

    #initialize counter for shuffX
    i = 0
    
    #pick a number between 10-20 for shuffX (number of shuffles)
    shuffX = secrets.randbelow(10) + 10

    #debug parameter to track Ace of Clubs
    Ac_index = []

    #The shuffling algorithm
    while i < shuffX:
        offset = int(len(un_shuffled) * .15)
        cut = int((secrets.randbelow(8)) + offset) 
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

    #assign card image to player's card
    image_dir = '<img src="/static/card_images/shuffle/'
    dex = un_shuffled.index(myCard) + 1
    strdex = str(dex)
    output = image_dir + strdex + '.svg"' + ' alt="' + myCard + '">'
    myCardImage = output

    #assign card image to computer's card
    image_dir = '<img src="/static/card_images/shuffle/'
    dex = un_shuffled.index(compCard) + 1
    strdex = str(dex)
    output = image_dir + strdex + '.svg"' + ' alt="' + compCard + '">'
    compCardImage = output

    #session counter
    counter = request.session.get('counter', 0)
    counter += 1
    request.session['counter'] = counter

    #take away quote marks for html insertion
    myCardImage = mark_safe(myCardImage)
    compCardImage = mark_safe(compCardImage)

    #store My Cards, images, ranks and debug vars to session
    request.session['myCard'] = myCard
    request.session['myCardValue'] = myCardValue
    request.session['myCardImage'] = myCardImage
    request.session['compCard'] = compCard
    request.session['compCardValue'] = compCardValue
    request.session['compCardImage'] = compCardImage
    request.session['Ac_index'] = Ac_index
    request.session['compStack'] = compStack
    request.session['playerStack'] = playerStack

    return render(
        request, 
        'one_card_wager/one_card_intro.html',
        {
        'startingStack': playerStack,
        'ante': ante,
        'betsize': betsize,
        }
    ) 

def one_card_wager(request):
    """Get session data from 'intro' page. HTML file shows 
    player their cards, and then gives the player two 
    options: check or bet"""

    #My Card and Computer Card session init + variables
    myCard = request.session.get('myCard')
    myCardValue = request.session.get('myCardValue')
    myCardImage = request.session.get('myCardImage')
    compCard = request.session.get('compCard')
    compCardValue = request.session.get('compCardValue')
    compCardImage = request.session.get('compCardImage')
    Ac_index = request.session.get('Ac_index')
    counter = request.session.get('counter')
    playerStack = request.session.get('playerStack')
    compStack = request.session.get('compStack')

    #both players ante
    pot = 0
    compStack -= ante
    pot += ante
    playerStack -= ante
    pot += ante

    #take away quote marks for html insertion
    myCardImage = mark_safe(myCardImage)
    compCardImage = mark_safe(compCardImage)

    #store My Card, Computer Card, images, ranks, and stacks to session
    request.session['myCard'] = myCard
    request.session['myCardValue'] = myCardValue
    request.session['myCardImage'] = myCardImage
    request.session['compCard'] = compCard
    request.session['compCardValue'] = compCardValue
    request.session['compCardImage'] = compCardImage
    request.session['Ac_index'] = Ac_index
    request.session['pot'] = pot
    request.session['playerStack'] = playerStack
    request.session['compStack'] = compStack

    return render(
        request,
        'one_card_wager/one_card_wager.html',
        {
            'myCardImage': myCardImage,
            'compCardImage': cardBackImage,
            'playerStack': playerStack,
            'compStack': compStack,
            'pot': pot,
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
    myCard = request.session.get('myCard')
    myCardImage = request.session.get('myCardImage')
    myCardValue = request.session.get('myCardValue')
    compCard = request.session.get('compCard')
    compCardImage = request.session.get('compCardImage')
    compCardValue = request.session.get('compCardValue')
    Ac_index = request.session.get('Ac_index')
    compAction = 0
    pot = request.session.get('pot')
    playerStack = request.session.get('playerStack')
    compStack = request.session.get('compStack')

    #take away quote marks for html insertion
    myCardImage = mark_safe(myCardImage)
    compCardImage = mark_safe(compCardImage)

    #Computer's strategy when checked to
    k100 = secrets.randbelow(100)
    if compCardValue >= 13:
        compAction = 'bet'
    elif compCardValue >= 9:
        if k100 > 25:
            compAction = 'bet'
    elif compCardValue <= 8:
        if k100 < 10:
            compAction = 'bet'
    else:
        compAction = None

    if compAction == 'bet':
        compStack -= betsize
        pot += betsize
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
        request.session['compStack'] = compStack
        request.session['playerStack'] = playerStack
        request.session['pot'] = pot

        return render(
            request,
            'one_card_wager/check.html',
            {
            'myCardImage': myCardImage,
            'compCardImage': cardBackImage,
            'counter': counter,
            'myCardValue': myCardValue,
            'compCardValue': compCardValue,
            'Ac_index': Ac_index,
            'myCard': myCard,
            'compCard': compCard,
            'compAction': compAction,
            'k100': k100,
            'playerStack': playerStack,
            'compStack': compStack,
            'pot': pot,
            }
        )

    else:
        compAction = None
        if myCardValue > compCardValue:
            result = "You Won the Showdown!"
            playerStack += pot
        if myCardValue < compCardValue:
            result = "You Lost the Showdown!"
            compStack += pot
        else:
            if myCardValue == compCardValue:
                result = "It's a Tie!"
                pot = (pot * .5)
                playerStack += pot
                compStack += pot

    
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
    request.session['playerStack'] = playerStack
    request.session['compStack'] = compStack
    request.session['pot'] = pot

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
            'playerStack': playerStack,
            'compStack': compStack,
            'pot': pot,
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
    playerStack = request.session.get('playerStack')
    compStack = request.session.get('compStack')
    pot = request.session.get('pot')

    #player called in order to reach this page
    playerStack -= betsize
    pot += betsize    

    myCardImage = mark_safe(myCardImage)
    compCardImage = mark_safe(compCardImage)

    if myCardValue == compCardValue:
        result = "It's a Tie!"
        pot = (pot * .5)
        playerStack += pot
        compStack += pot
    elif myCardValue > compCardValue:
        result = "You Won the Showdown!"
        playerStack += pot
    elif myCardValue < compCardValue:
        result = "You Lost the Showdown!"
        compStack += pot

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
    request.session['playerStack'] = playerStack
    request.session['compStack'] = compStack
    request.session['pot'] = pot

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
            'playerStack': playerStack,
            'compStack': compStack,
            'pot': pot,
        }
    )

def fold(request):
    """player folds to computer's bet"""

        #get variables from session
    counter = request.session.get('counter')
    pot = request.session.get('pot')
    compCard = request.session.get('compCard')
    playerStack = request.session.get('playerStack')
    compStack = request.session.get('compStack')
    Ac_index = request.session.get('Ac_index')
    k100 = request.session.get('k100')
    result = "You lose the pot!"

    compStack += pot

    request.session['compStack'] = compStack
    request.session['playerStack'] = playerStack

    return render(
        request,
        'one_card_wager/fold.html',
        {
            'pot': pot,
            'counter': counter,
            'playerStack': playerStack,
            'compStack': compStack,
            'compCard': compCard,
            'Ac_index': Ac_index,
            'k100': k100,
            'result': result,
        }
    )

def bet(request):
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
    pot = request.session.get('pot')
    playerStack = request.session.get('playerStack')
    compStack = request.session.get('compStack')

    playerStack -= betsize
    pot += betsize

    k100 = secrets.randbelow(100)
    if compCardValue > 12:
        compAction = 'call'
    elif compCardValue >= 9:
        if k100 > 25:
            compAction = 'call'
    else:
        compAction = None

    if compAction == 'call':
        compStack -= betsize
        pot += betsize
        if myCardValue == compCardValue:
            result = "It's a Tie!"
            pot = (pot * .5)
            playerStack += pot
            compStack += pot
        elif myCardValue > compCardValue:
            result = "You Won the Showdown!"
            playerStack += pot
        elif myCardValue < compCardValue:
            result = "You Lost the Showdown!" 
            compStack += pot

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
        request.session['playerStack'] = playerStack
        request.session['compStack'] = compStack

        #take away quote marks for html insertion
        myCardImage = mark_safe(myCardImage)
        compCardImage = mark_safe(compCardImage)

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
            'pot': pot,
            'playerStack': playerStack,
            'compStack': compStack,
        }
    )

    else:
        #get variables from session
        counter = request.session.get('counter')
        request.session['counter'] = counter
        Ac_index = request.session.get('Ac_index')
        k100 = request.session.get('k100')
        result = "You Won the Pot!"
        playerStack += pot

        request.session['playerStack'] = playerStack
        request.session['compStack'] = compStack
        request.session['compCard'] = compCard

        return render(
            request,
            'one_card_wager/compFold.html',
            {
            'counter': counter,
            'Ac_index': Ac_index,
            'k100': k100,
            'result': result,
            'pot': pot,
            'playerStack': playerStack,
            'compStack': compStack,
            'compCard': compCard,
        }
    )        
