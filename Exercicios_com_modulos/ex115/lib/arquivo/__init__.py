# from ex115.lib.interfce import *


def linha(tam=42):
    return '-'*42


def Cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def arquivoExiste(name):
    try:
        a = open(name, 'rt') #abrir(nomedoarquivo, 'para leitura' ------ 'rt' read
        a.close() # Fechar o arquivo
    except FileNotFoundError: #exceção para arquivo não existe/ounão encontrado
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+') #abrir(nomedoarquivo, 'escrever/+ = se não tem, criar o arquivo' ----- 'wt' escrever
        a.close()
    except Exception as erro:
        print(f"Houve um erro na criaçã odo arquivo\n Erro:{erro.__class__}")
    else:
        print("Arquivo Criado com sucesso")


def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
       print('Erro ao ler o Arquivo')
    else:
        cad = list()
        Cabecalho("Pessoas Cadastradas")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:3>} anos')
    finally:
        a.close()


def CadastrarArquivo(arq, nome='desconhecido', idade = 0):
    try:
        a = open(arq, 'at') #a de apend(colocar coisa no arquivo
    except:
        print("Houve um erro na abertura do arquivo")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Houve um ERRO na hora de escrever os dados")
        else:
            print(f"Novo Registro de {nome} adcionado.")