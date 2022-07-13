#Al: Programa que leia uma expreção qualquer que use parenteses.
# no final o programa diz se a expreção está válida pelo uso dos parenteses
#autor: Lucas Borguezam
#data:

#Import

#Inicio
exp = str(input("Informe uma expreção matemática\nObs: usando apenas '()'\n"))
p1 = p2 =0
for item in range(len(exp)):
    if exp[item] == '(':
        p1 +=1
    elif exp[item] == ')':
        p2 +=1
if (p1+p2)%2==0:
    print("A Expreção é válida")
else:
    print("A expressão não é válida")

print(f"{'OU':^20}")
exp = str(input("Informe uma expreção matemática\n"))
pilha = []
# em uma lista quando veriicada, encontrando o '(' vai adicionar '(' na lista pilha[].
# quando verificar o próximo ')' vai deletar um '(' da lista pilha[] se a lista tiver um item cadastrado.
# se não, vai adcionar o ")" e parar a verificação pois se começa com ")" não da pra fechar e torna inválida
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão é Válida!")
else:
    print("Sua expressão está errada!")
#fim
