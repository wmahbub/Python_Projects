import random
import numpy as np

def card_draw(num):
    """ Draw any number of cards at random. """
    cards=[]
    counter= 0
    
    while counter < num:
        a = random.choices(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
        b = random.choices(['D', 'H', 'C', 'S'])
        
        hand= [i + j for i,j in zip(a,b) ]
        
        if hand[0] not in cards:
            cards.append(hand[0])
            counter +=1
        
    return cards

# print(card_draw(12))


def player_draw(players,num):
    """ Draws for number of players. """
    
    cards = card_draw(players * num)
    cards = random.sample(cards, len(cards))
    
    group = [ cards[i*num : (i + 1) * num] for i in range((len(cards) + num - 1) // num) ] 
 
    return group

round1= player_draw(4,5)
print(round1)

def value_sep(lst):
    """ Seprates values from houses. """
    
    final= []
    
    for i in range(len(lst)):
        
        player= []
        
        for j in range(len(lst[i])):
            
            if len(lst[i][j]) == 2:
                player.append(lst[i][j][0])
            
            else :
                player.append(lst[i][j][0:2])
    
        final.append(player)
    
    return final 


b = value_sep(round1)
print(b)
    
def value_sum(lst):
    """ Checks how many pairs are there and sums the scores. """
    
    freq = {}
    
    for elem in lst:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1

    return freq


print(value_sum(['5', '7', '7', 'A', 'J']))
