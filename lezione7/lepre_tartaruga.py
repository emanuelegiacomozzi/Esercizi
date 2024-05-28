import random

def posizioni(posizione_t, posizione_h):
    percorso = ['_']*70
    if posizione_t == posizione_h:
        percorso[posizione_t - 1] = 'OUCH!!!'
    else:
        percorso[posizione_t - 1] = 'T'
        percorso[posizione_h - 1] = 'H'
    print(''.join(percorso))

def mosse_tartaruga(tartaruga,meteo):
    i:int = random.randint(1,10)
    if 1 <= i <= 5:
        tartaruga += 3
    elif 6 <= i <= 7:
        tartaruga -= 6
    elif i < 1:
        tartaruga = 1
    else:
        tartaruga += 1
    if meteo == "piogga":
        tartaruga -= 2
    return tartaruga



def mosse_lepre(lepre,meteo):
    i:int = random.randint(1,10)
    lepre = 0
    if 1 <= i <= 2:
        lepre = 0
    elif 3 <= i <= 4:
        lepre += 9
    elif i == 5:
        lepre -= 12
    elif 6 <= i <= 8:
        lepre += 1
    elif 9 <= i <= 10:
        lepre -= 2
    elif i < 1:
        lepre = 1
    if meteo == "piogga":
        lepre -= 2
    return lepre


def  gara():
    posizione_t = 1
    posizione_h = 1
    meteo = "soleggiato"
    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")
    while True:
            posizione_t = mosse_tartaruga(posizione_t, meteo)
            posizione_h = mosse_lepre(posizione_h, meteo)
            posizioni(mosse_tartaruga, mosse_lepre)
            if posizione_t >= 70:
                print("TORTOISE WINS! || VAY!!!")
                break
            elif posizione_h >= 70:
                print("HARE WINS || YUCH!!!")
                break
            elif posizione_h >= 70 and posizione_t >= 70:
                print("IT'S A TIE.")
                break
gara()




