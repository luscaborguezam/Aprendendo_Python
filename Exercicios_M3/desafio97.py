#Al: Função escreva(), com parametro recebido pelo usuário. ao final mostrar um cabeçãrio com a str recebida
#autor: Lucas Borguezam
#data:

#Import

#Inicio
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~'* tam)



escreva(str(input("Escreva: ")))
#fim
