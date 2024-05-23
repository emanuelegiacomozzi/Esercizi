#esercizio 1
def transform(x: int) -> int:
    if x % 2 == 0:
        return x // 2
    else:
        return (x*3)-1
print(transform(9))

#esercizio 2
def calcola_stipendio(ore_lavorate:int):
    if ore_lavorate <= 40:
        ore_lavorate *= 10
        return ore_lavorate
    else:
        ore_in_più = ore_lavorate-40
        ore_in_più *= 15
        ore_incrementate = (40*10) + ore_in_più
        return ore_incrementate
print(calcola_stipendio(45))

#esercizio 3
def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1,8):
        print(i)
    print()

    print("Sequenza b):")
    for i in range(3,24,5):
        print(i)
    print()

    print("Sequenza c):")
    for i in range(20,-10,-11):
        print(i)
    print()

    print("Sequenza d):")
    for i in range(19,52,8):
        print(i)
    print()
    
    return

#esercizio 4

def integerPower(base:int,esponente:int):
    if esponente <= 0 :
        return False
    
    base_per_esponente = base**esponente
    return base_per_esponente
print(integerPower(3,-2))

#esercizio 5
import math
def hypotenuse(cateto1:float, cateto2:float):
    ipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return ipotenusa
print(hypotenuse(8.0, 15.0))

#esercizio 6
def frequency_dict(elements:list):
    dizionario = {}
    for element in elements:
        x = elements.count(element)
        dizionario[element] = x
    return dizionario
print(frequency_dict([2,3,4,2,3,4,4]))

#esercizio 7
def seconds_since_noon(ore:int,min:int,sec:int):
    secondi_totali = ore*3600 + min*60 + sec
    return secondi_totali

def time_difference(ora1:int, min1:int, sec1:int, ora2:int, min2:int, sec2:int):
    secondi_totali = seconds_since_noon(ora1, min1, sec1)
    secondi_totali2 = seconds_since_noon(ora2, min2, sec2)
    if secondi_totali2 > secondi_totali:
        return secondi_totali2 - secondi_totali
    else:
        return secondi_totali - secondi_totali2
print(time_difference(1, 0, 0, 3, 15, 30))

#esercizio 8
#tempo 0 ----> altezza zero, velocita = 100 cm/s
#s1 --> altezza = altezza + velocità
#s1 ---> velocità = velocità-96
#se valore altezza < 0 ---> altezza * -0.5, velocità*-0,5
def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    while rimbalzi < 5:
        print(f"Tempo: {tempo} Altezza: {altezza}")
        altezza += velocita
        velocita -= 96 
        tempo += 1

        if altezza < 0:
            altezza *= -0.5
            velocita *= -0.5   
            print(f"Tempo: {tempo} Rimbalzo!")
            rimbalzi += 1 
            tempo += 1
rimbalzo()
        



    
    

