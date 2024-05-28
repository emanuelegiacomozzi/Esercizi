import random

def posizioni(percorso, tartaruga, lepre):
    percorso[0] =  tartaruga, lepre
    return percorso

percorso = ['_']*70
tartaruga = 'T'
lepre = 'H'
print(posizioni(percorso,tartaruga,lepre))

def mosse_tartaruga(posizione_t):
    i:int = random.randint(1,10)
    if 1 <= i <= 5:
        posizione_t += 3
    elif 6 <= i <= 7:
        posizione_t -= 6
    elif i < 1:
        posizione_t = 1
    else:
        posizione_t += 1
    return posizione_t
posizione_t = 0
print(mosse_tartaruga(posizione_t))


def mosse_lepre(posizione_h):
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
posizione_h = 0
print(mosse_lepre(posizione_h))

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




