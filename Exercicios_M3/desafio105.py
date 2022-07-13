#Al:Notas(), receber várias notas, e retorna um dicionário com as seguintes informações:
# qtd notas
# maior nota
# menor nota
# média da turma
# Situação(opcional)
#autor: Lucas Borguezam
#data:

#Import

#Inicio
def Notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: tupla que recebe as notas informadas.
    :param sit: (Opcional) indica se deve ou não adicionar a situação.
    :return: Dicionário r com várias informações dobre a  situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] < 5:
            r['situação'] = 'RUIM'
        elif r['média'] < 7:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'BOA'
    return r


resp = Notas(1.5, 5.5, 3, 6.5, sit=True)
print(resp)
help(Notas)
# fim
