print('              CONTROLE DE TERRENOS')
print(50*'-')
def area(a, b):
    d = a * b
    print(f'A área do terreno de {a} x {b} é {d}m²')


largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(a=largura, b=comprimento)





'''def dobra(valores):
    pos = 0
    while pos < len(valores):
        valores[pos] *= 2
        pos += 1


valores = [1, 5, 9, 7, 20, 10, 15]
dobra(valores)
print(valores[0:len(valores)])'''