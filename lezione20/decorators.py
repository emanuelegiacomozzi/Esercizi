def ciao(name:str)->str:

    return f"Ciao, {name}"

def salve(name:str)->str:
    return f"Salve, {name}"

def saluta(func)->str:

    return func("Bob")

print(saluta(ciao))
print(saluta(salve))

#######################################

def parent():

    print("Sono in parent!")

    def first_child():

        print("Sono in First Child!")
    
    #def second_child():

        #print("Sono in Second Child")
    
    #second_child()
    #second_child()
    return first_child

print(parent())

##########################################

def decorator(func):

    def wrapper():

        print(f"Prima di func")

        func()

        print(f"Dopo func")
    
    return wrapper

def ciao():

    print(f"Ciao!")

ciao = decorator(ciao)

ciao()


############################################

def decorator(func):

    def wrapper(*args):

        import time

        start = time.time()

        func()

        print(f"Time elapsed: {time.time() - start}") #tempo esecuzione funzione
    
    return wrapper

def ciao():

    print(f"Ciao")

ciao = decorator(ciao)

ciao()


