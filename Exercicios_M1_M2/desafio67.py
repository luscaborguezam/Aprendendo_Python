#Al: Tabuada para n numeoros que forem digitados, numero negativo é o break
#autor: Lucas Borguezam
#data:

#Import
v = 0
#Inicio
while True:
    v = int(input("De qual número deseja receber a tabuada?\n"))
    if v < 0:
        break
    print("-"*20)
    for t in range(1, 11):
        print(f"{v}x{t}={v*t}")
    print("-" * 20)
print("fim")
#fim
