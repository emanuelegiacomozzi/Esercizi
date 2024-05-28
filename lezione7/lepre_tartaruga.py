import random

def posizioni(percorso, posizione_t, posizione_h):
    percorso[0] =  posizione_t, posizione_h
    return percorso

percorso = ['_']*70
posizione_t = 'T'
posizione_h = 'H'
print(posizioni())

def mosse_tartaruga():
    i:int = random.randint(1,10)
    posizione_t = 0
    if 1 <= i <= 5:
        posizione_t += 3
    elif 6 <= i <= 7:
        posizione_t -= 6
    elif i < 1:
        posizione_t = 1
    else:
        posizione_t += 1
    return posizione_t


def mosse_lepre():
    i:int = random.randint(1,10)
    posizione_h = 0
    if 1 <= i <= 2:
        posizione_h = 0
    elif 3 <= i <= 4:
        posizione_h += 9
    elif i <= 5:
        posizione_h -= 12
    elif 6 <= i <= 8:
        posizione_h += 1
    elif 9 <= i <= 10:
        posizione_h -= 2
    elif i < 1:
        posizione_h = 1
    return posizione_h

def inizia_gara():
    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")

while True:
    if posizione_t >= 70:
        print("TORTOISE WINS! || VAY!!!")
        break
    elif posizione_h >= 70:
        print("HARE WINS || YUCH!!!")
        break
    elif posizione_h >= 70 and posizione_t >= 70:
        print("IT'S A TIE.")
        break




