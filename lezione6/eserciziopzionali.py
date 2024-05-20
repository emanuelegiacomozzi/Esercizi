'''
Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
'''
def dict_value(dizionario:dict, valore:int):
    for key,value in dizionario.items():
        if value == valore:
            return key
    return None
dizionario = {"A":1,"B":2,"C":3}
valore = 3
print(dict_value(dizionario,valore))

'''
Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.
'''
def chiavi_valori(dizionario:dict):
    dizionario2 = {}
    for key,value in dizionario.items():
        if value not in dizionario2:
            dizionario2[value] = key
    return dizionario2
dizionario = {"A":1, "B":2, "C":3, "D":4, "E": 1}
print(chiavi_valori(dizionario))
        
'''
Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari, e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.
'''
def lista_numeri(lista:list):
    lista2 = []
    fattore = int(input("Inserisci un fattore: "))
    for num in lista:
        if num % 2 == 0:
            num *= fattore
            lista2.append(num)
    return lista2
lista = [1,4,2,5,6]
print(lista_numeri(lista))

'''
Scrivi una funzione che determina se un numero è 'magico'. Un numero è considerato magico se è divisibile per 4 ma non per 6.
'''
def numero_magico(numero:int):
    if numero % 4 == 0 and numero % 6 != 0:
        return f"{numero} è un numero magico"
    else: 
        return f"{numero} non è un numero magico"
numero = int(input("Inserisci un numero: "))
print(numero_magico(numero))

'''
 Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3.
'''
def numeri_divisibili(lista:list[int]):
    somma = 0
    for num in lista:
        if num % 2 == 0 and num % 3 == 0:
            somma += num
    return f"La somma è: {somma} "
lista = [2,24,7,6,9,8,10,34,25,65,12,3]
print(numeri_divisibili(lista))

'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
'''
def negozio(prodotti:dict[str,float]):
    prodotti2:dict = {}
    for prodotto,prezzo in prodotti.items():
        if prezzo > 20:
            prezzo_scontato = prezzo*10 / 100
            prodotti2[prodotto] = prezzo_scontato
    return prodotti2
prodotti = {"Fazzoletti": 2.80, "Pennarelli": 10, "Quadri":21, "Cover":25}
print(negozio(prodotti))

'''
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
'''

