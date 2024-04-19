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
x= int(input("Inserisci un numero: "))
check_value(x)

#esercizio 3

def check_length(x:str):
    if len(x) > 10:
        print(f"La lunghezza di {x} è maggiore di 10")
    elif len(x) < 10:
        print(f"La lunghezza di {x} è minore di 10")
    else: 
        print(f"La lunghezza di {x} è uguale a 10")
    return x
x = input("Inserisci una stringa: ")
check_length(x) 

#esercizio 4

def print_numbers(l:list):
    for i in l:
        print(i)
    return i
l = [1,2,3,4]
print_numbers(l)