def linha(tam=42):
    return '-'*42


def Cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def Menu(lista):
    Cabecalho("Menu Principal")
    for c, i in enumerate(lista):
        print(f"\033[33m{c+1}\033[m - \033[34m{i}\033[m")
    print(linha())
    opc = LeiaInt("\033[33mSua Opção: \033[m")
    return opc

def LeiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (TypeError, ValueError):
            print("\033[1;31mPor favor Digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mVocê não digitou nada. Tente novamente...\033[m")
            continue
        else:
            return i
            break