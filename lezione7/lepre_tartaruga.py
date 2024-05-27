import random

def posizioni():
    percorso = ['_']*70
    posizione_t = 'T'
    posizione_h = 'H'
    percorso[0] =  posizione_t, posizione_h
    return percorso
print(posizioni())

def mosse_tartaruga():
    i:int = random.randint(1,10)
    posizione_t = 0
    if 1 <= i <= 5:
        posizione_t += 3
    elif 6 <= i <= 7:
        posizione_t -= 6
    elif i < 1:
        posizione_t = 0
    else:
        posizione_t += 1
    return posizione_t
print(mosse_tartaruga())

def mosse_lepre():
    i:int = random.randint(1,10)
    posizione_h = 0
    if 1 <= i <= 2:
        posizione_h = 0
    elif 3 <= i <= 4:
        posizione_h += 9
    elif 5 <= i <= 8:
        posizione_h += 1
    elif 8


