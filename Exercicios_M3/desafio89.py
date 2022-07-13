#Al: Programa que leia 2 notas  de vários alunos, e guarde em uma lista composta
# mostrar ao final o boletim contendo a media e as notas individualmente
#autor: Lucas Borguezam
#data:

#Import

#Inicio
disciplina = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    disciplina.append([nome, [nota1, nota2], media])
    cond = str(input("Deseja continuar? [S/N]: ").strip().lower()[0])
    if cond == 'n':
        break
print("-="*50)
print(f"{'N°.':<4} {'NOME':<10} {'Média':>8}\n"
      f"{'-'*30}")
for c, aluno in enumerate(disciplina):
    print(f"{c:<4} {aluno[0]:<10} {aluno[2]:>8.1f}")
while True:
    print("--"*50)
    alu = int(input("Mostrar nota de qual aluno? (999 interrompe)"))
    if alu == 999:
        break
    elif alu >= 0 and alu < len(disciplina):
        print(f"Notas de {disciplina[alu][0]} são: {disciplina[alu][1]}")
    else:
        print("Aluno não existe ou não foi encontrado.")
print(f"{'Fim':>50}")

#fim
