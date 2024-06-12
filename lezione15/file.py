file = open('lezione15/file.txt')

with open(f'lezione15/file.txt') as file:

    print(file)
    
try:

    file.readline()
    print("Sono nella try")
    raise Exception("Eccezione")

except Exception:

    print("Sono nella except")

finally:

    print("Sono nella finally")
    file.close()