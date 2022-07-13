from lib import interfce
from lib import arquivo
from time import sleep

arq = "cadastro.txt"

if not arquivo.arquivoExiste(arq):
# print("Aquivo Existe")
# else:
    # print("Arquivo não existe ou não foi encontrado")
    arquivo.CriarArquivo(arq)

while True:
    res = interfce.Menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema\n"])
    if res == 1:
        arquivo.LerArquivo(arq)
    elif res == 2:
        interfce.Cabecalho("Novo Cadastro".upper())
        nome = str(input("Nome: "))
        idade = interfce.LeiaInt("Idade: ")
        arquivo.CadastrarArquivo(arq, nome, idade)
    elif res == 3:
        print("Saindo do sistema...")
        break
    else:
        print("\033[1;31mOpção Inválida\033[m")
    sleep(0.3)
