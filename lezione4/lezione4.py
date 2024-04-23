#esercizio 1

def subtract(x:float, y:float):
    sub:str = x - y
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
x:int= int(input("Inserisci un numero: "))
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
x:str = input("Inserisci una stringa: ")
check_length(x) 

#esercizio 4

def print_numbers(l:list):
    for i in l:
        print(i)
    return i
l:list = [1,2,3,4]
print_numbers(l)

#esercizio 5

def check_each(l:list):
    for i in l:
        if i > 5:
            print(f"{i} è maggiore di 5")
        elif i < 5:
            print(f"{i} è minore di 5")
        else: 
            print(f"{i} è uguale a 5")
    return i
l:list = [2, 5, 7, 8, 9]
check_each(l)

#esercizio 6
def add_one(n:int):
    return n+1
n:int = int(input("Inserisci un numero: "))
print(add_one(n))
def add_one_to_list(l:list):
    new_list:list = []
    for n in l:
        x = n + 1 
        new_list.append(x)
    return new_list
l:list = [4, 4, 11]
print(add_one_to_list(l))

#esercizi 

