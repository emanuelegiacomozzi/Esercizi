import os #operative system

sRoot = input("Inserisci directory in cui cercare")
sParola = input("Inserisci parola da cercare")
sOutDir = input("Inserisci directory di output")

for root,dirs,files in os.walk(sRoot):
    print(f"Sto guardando {root} che contiene {len(dirs)} subdir e {len(files)} file")
    for file in files:
        print(f"Devo vedere se {file} contiene {sParola}")