def aumentar(v=0, f=0, showf=False):
    resp = v + (v * (f / 100))
    return resp if showf is False else moeda(resp)


def diminuir(v=0, f=0, showf=False):
    resp = v - (v * (f/100))
    return resp if showf is False else moeda(resp)


def dobro(v=0, showf=False):
    resp = v * 2
    return resp if showf is False else moeda(resp)


def metade(v=0, showf=False):
    resp = v/2
    return resp if showf is False else moeda(resp)


def moeda(preco=0,moeda='R$'):
    return f'{moeda} {preco:>.2f}'.replace('.',',')


def resumo(v=0,a=0,r=0):
    analisado = v
    dobro = v * 2
    meta = v / 2
    aum = v + (v * (a / 100))
    desc = v - (v * (r / 100))
    return f'{40*"-"}\n' \
           f'{"RESUMO DE PREÇO".center(40)}\n' \
           f'{40*"-"}\n' \
           f'Preço analisado:\t\t\t{moeda(v)}\n'\
           f'Dobro do preço:\t\t\t\t{moeda(dobro)}\n'\
           f'Metade do preço:\t\t\t{moeda(meta)}\n'\
           f'{a}% de aumento:\t\t\t\t{moeda(aum)}\n'\
           f'{r}% de redução:\t\t\t\t{moeda(desc)}\n' \
           f'{40*"-"}'




