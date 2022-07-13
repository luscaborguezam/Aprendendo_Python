#Al: Função para calcular fatorial, com parametro show(False/True): mostra o calculo
#autor: Lucas Borguezam
#data:

#Import

#Inicio


def Fatorial(n=1, show=False):
    """
    ->Calcula o Fatorial de um número
    :param n: Número a ser calculado
    :param show: (Opcional) mostra a fatoração.
    :return: Valor fatorial de um número n
    """
    f = 1
    while n > 0:
        f *= n
        if show == True:
           print(f"{n} X " if n > 1 else f"{n} = ", end='')
        n -= 1
    return f


print("--" * 25)
c = int(input("Número: "))
while True:
    s = str(input("deseja ver a conta? [s/n]: ")).strip().lower()[0]
    if s in 'sn':
        if s == 's':
            m = True
            break
        else:
            m = False
            break
    else:
        print("Erro! Digite 's' ou 'n' para continuar.")
print(f"{c}! = ", end='')
print(Fatorial(c, show=m))
#fim
