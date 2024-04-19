#esercizio 1

def subtract(x:float, y:float):
    sub = x - y
    return sub
print(subtract(10,8))

#esercizio 2

def check_value(x:int):
    if x > 5:
        print(f"{x} è maggiore di 5")
    elif x < 5:
        print(f"{x} è minore di 5")
    else:
        print(f"{x} è uguale a 5")
    return x
x:int = int(input("Inserisci un numero: "))
check_value(x)