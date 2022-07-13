def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg).strip())
        except (ValueError, TypeError):
            print(f"\033[1;31mPor favor, Digite um número inteiro válido\033[m")
            continue #Joga a sequencia da execução para o inicio do while
        except (KeyboardInterrupt):
            print("\033[0;31m\nUsuário preferiu não digitar um valor\033[m")
            return 0
            break
        else:
            return valor
            break


def leiaFloat(msg):
    while True:
        try:
            valor = float(input((msg)).strip().replace(",", '.'))
        except (ValueError, TypeError):
            print("\033[0;31mPorfavor digite um número real válido\033[m")
            continue #Joga a sequencia da execução para o inicio do while
        except (KeyboardInterrupt):
            print("\033[0;31m\nUsuário preferiu não digitar um valor\033[m")
            return 0
            break
        else:
            return float(valor)
            break
