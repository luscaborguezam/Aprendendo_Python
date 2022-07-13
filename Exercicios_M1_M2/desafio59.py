#Al: Calculadora com while
#autor: Lucas Borguezam
#data:

#Import

#Inicio
op = 0
v1 = float(input("1° Valor: "))
v2 = float(input("2° valor: "))
while op != 5:
    print("-----Calculadora -----")
    print("[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair")
    op = int(input("Qual opção deseja?\n>>"))
    if op == 1:
        print("SOMA")
        print("Resultado: {}".format(v1+v2))
    elif op == 2:
        print("Multiplicação")
        print("Resultado: {}".format(v1*v2))
    elif op == 3:
        print("MAIOR")
        if v1 == v2:
            print("Valores iguais")
        else:
            print("1° valor inserido {}".format(v1) if v1 > v2 else "2° valor inserido {}".format(v2))
    elif op == 4:
        print("Novos números")
        v1 = float(input("1° Valor: "))
        v2 = float(input("2° valor: "))
    elif op == 5:
        print("Finalizando...")
    else:
        print("Opção inválida")
print("fim")
#fim
