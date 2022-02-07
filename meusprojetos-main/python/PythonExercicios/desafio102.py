def fatorial(num, show=False):
    """
    -> Essa função calcula o fatorial do número escolhido.
    :param num: É o número escolhido.
    :param show: Permite escolher se quer ou não mostrar o fatorial por extenso na tela.
    :return: O valor do fatorial do número escolhido.
    """
    f = 1
    print(f'O fatorial de {num} é:', end=' ')
    for p in range(num, 0, -1):
        if show:
            print(p, end=' ')
            if p > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= p
    return f


print(fatorial(5,show=True))
#num = int(input('Digite um número para saber seu fatorial: '))
#show = input('Deseja mostrar o calculo todo na tela [S/N]?: ')
#help(fatorial)


