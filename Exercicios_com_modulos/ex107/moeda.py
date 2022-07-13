def Aumentar(v, p):
    """
    ->Função que aumenta v em p %
    :param v: valor inserido
    :param p: porcentagem inserida
    :return: retarna valor com o aumento
    """
    a = v + (v*(p / 100))
    return a


def Diminuir(v, p):
    """
    ->Função que diminui v em p %
    :param v: valor inserido
    :param p: porcentagem inserida
    :return: retarna valor com o desconto
    """
    d = v - (v*(p / 100))
    return d


def Dobro(v):
    """
    ->Função que dobra v
    :param v: valor inseido
    :return: retorna o dobro de v
    """
    return v*2


def Metade(v):
    """
    ->Função que divide v
    :param v: valor inseido
    :return: retorna a metade de v
    """
    return v/2
