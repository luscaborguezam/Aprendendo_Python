def Aumentar(v=0, p=0, op=False):
    """
    ->Função que aumenta v em p %
    :param v: valor inserido
    :param p: porcentagem inserida
    :param op: (opcional) retorno Formatado ou não
    :return: retarna valor com o aumento
    """
    a = v + (v * (p / 100))
    return a if op is False else Moeda(a)


def Diminuir(v=0, p=0, op=False):
    """
    ->Função que diminui v em p %
    :param v: valor inserido
    :param p: porcentagem inserida
    :param op: (opcional) retorno Formatado ou não
    :return: retarna valor com o desconto
    """
    d = v - (v * (p / 100))
    return d if op is False else Moeda(d)


def Dobro(v=0, op=False):
    """
    ->Função que dobra v
    :param v: valor inseido
    :param op: (opcional) retorno Formatado ou não
    :return: retorna o dobro de v
    """
    res = v * 2
    return res if op is False else Moeda(res)


def Metade(v=0, op=False):
    """
    ->Função que divide v
    :param v: valor inseido
    :param op: (opcional) retorno Formatado ou não
    :return: retorna a metade de v
    """
    res = v / 2
    return res if op is False else Moeda(res)


def Moeda(p=0, moeda="R$"):
    """
    ->Função que formata o valor
    :param p: valor inserido/processado
    :param moeda: Sigla da moeda usada
    :return: retorna o valor formatado
    """
    return f"{moeda}{p:.2f}".replace('.', ',')


def Resumo(v, pa=10, pr=5):
    """
    ->Função que resume todas as demais
    :param v: valor inserido
    :param pa: porcentagem de aumento
    :param pr: Porcentagem de redução
    :return: retorna varias informações sobre o valor
    """
    print(f"{'-' * 30}\n{'RESUMO DO VALOR'.center(30)}\n{'-' * 30}\n",
          f"{'Preço nalisado:':<15} \t{Moeda(v):<}\n",
          f"{'Dobro do preço:':<15} \t{Dobro(v, True):<}\n",
          f"{'Metade do preço:':<15} \t{Metade(v, True):<}\n",
          f"{pa}{'% de aumento:':<15} \t{Aumentar(v, pa, True):<}\n",
          f"{pr}{'% de redução:':<15} \t{Diminuir(v, pr, True):<}\n",
          f"{'--' * 20}")
