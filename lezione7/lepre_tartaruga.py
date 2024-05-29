import random

def posizioni(posizione_t, posizione_h):
    percorso = ['_']*70
    if posizione_t == posizione_h and posizione_t >= 1:
            percorso[posizione_t - 1] = 'OUCH!!!'
    else:
        if posizione_h >= 1:
            percorso[posizione_h - 1] = 'H'
        if posizione_t >= 1:
            percorso[posizione_t - 1] = 'T'
    print(''.join(percorso))

def mosse_tartaruga(tartaruga):
    i:int = random.randint(1,10)
    if 1 <= i <= 5:
        tartaruga += 3
    elif 6 <= i <= 7:
        tartaruga -= 6
    elif 8 <= i <= 10:
        tartaruga += 1
    if tartaruga < 1:
        tartaruga = 1
    if tartaruga > 70:
        tartaruga = 70
    return tartaruga



def mosse_lepre(lepre):
    i:int = random.randint(1,10)
    lepre = 0
    if 1 <= i <= 2:
        pass
    elif 3 <= i <= 4:
        lepre += 9
    elif i == 5:
        lepre -= 12
    elif 6 <= i <= 8:
        lepre += 1
    elif 9 <= i <= 10:
        lepre -= 2
    if lepre < 1:
        lepre = 1
    if lepre > 70:
        lepre = 70
    return lepre

def gara():
    posizione_t = 1
    posizione_h = 1
    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")

    while True:
        posizione_t = mosse_tartaruga(posizione_t)
        posizione_h = mosse_lepre(posizione_h)
        posizioni(posizione_t, posizione_h)
        if posizione_h >= 70 and posizione_t >= 70:
            print("IT'S A TIE.")
            break
        elif posizione_t >= 70:
            print("TORTOISE WINS! || VAY!!!")
            break
        elif posizione_h >= 70:
            print("HARE WINS || YUCH!!!")
            break
        
gara()




