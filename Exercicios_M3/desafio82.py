#Al: lista revebe varios numeros.
# Criar suas listas que receberão valores pares e mpares da 1° lista
# mostre as 3 listas
#autor: Lucas Borguezam
#data:

#Import

#Inicio
lista=[]
par = []
impar = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    # if n%2==0 and n not in par:
    #         par.append(n)
    # elif n%2!=0 and n not in impar:
    #     impar.append(n)
    #condição de parada
    cond = ' '
    while cond not in 'sn':
        cond = str(input("Deseja continuar? [S/N]: "))
    if cond == 'n':
        break
for v in lista:
    if v%2==0:
        par.append(v)
    else:
        impar.append(v)
print(f"Valores inseridos:{lista}\n"
      f"Par:{par}\n"
      f"Impar:{impar}")
#fim
