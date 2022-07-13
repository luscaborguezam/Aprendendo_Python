#Al: leiaint(), validar e aceitar apenas valores numéricos
#autor: Lucas Borguezam
#data:

#Import

#Inicio


# def LeiaInt(var=' '):
#     """
#     ->Validando entrada de dados (números inteiros)
#     :param var: número que o usuário digitar
#     :return: número inteiro var
#     """
#     var = str(input("Digite um número: "))
#     if var.strip() == '':
#         var = 'a'
#     while var.isalpha():
#         print("\033[1;31mErro! Digite um número inteiro válido\033[m")
#         var = input("Digite um número: ")
#         if var.isnumeric():
#             int(var)
#         if var.strip() == '':
#             var = 'a'
#     print(f"Você digitou o número {var}")


#corrçãp
def LeiaInt(msg):
    """
    ->Validando entrada de dados (números inteiros)
    :param msg: mensagem para usuário
    :return: retorna apenas valores numéricos
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        if ok:
            break
    return valor


#Código principal
num = LeiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {num}")
#fim
