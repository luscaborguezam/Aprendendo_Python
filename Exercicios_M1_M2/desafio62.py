#Al: exercicio 61 com loop
#autor: Lucas Borguezam
#data:

#Import

#Inicio
primeiro = int(input(print("1° Termo: ")))
razao = int (input(print("Razão: ")))
termo = primeiro # termo começa com o primeiro termo
cont = 1
qtdTermos = 10
while cont <= qtdTermos:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
    if cont > qtdTermos:
        maisTermos = int(input("\nQuantos termos a mais gostaria de ver? "))
        if maisTermos > 0:
                qtdTermos += maisTermos
        else:
                print("Finalizando...")
print("Progressão foi finalizada com {} termos.".format(cont))

#correção
primeiro = int(input(print("1° Termo: ")))
razao = int (input(print("Razão: ")))
termo = primeiro # termo começa com o primeiro termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais?\n"))
print("Progressão finalizada com {} termos mostrados".format(total))
#fim
