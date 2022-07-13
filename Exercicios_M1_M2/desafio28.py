#Al: Programa que a máquina calcule um numero randomico entre 0 e 5, e peça para o usuário acertar.
#autor: Lucas Borguezam
#data:18032022

#Import
import  random
#Inicio
nr = random.randint(0, 5)
print('--?--'*20)
print("Vou pensar em um número entre 0 e 5. Tente advinhar...")
print('--??--'*20)
n1 = int(input("Em que número pensei?? "))
if (n1>=0) or (n1<=5):
    print('Acertou'if n1==nr else'Errou , foi escolhido o numero {}'.format(nr))
else:
    print("Número digitado inválido")

#fim
