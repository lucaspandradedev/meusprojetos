lista = []
pmax = []
pmin = []
for n in range(0, 5):
    num = (int(input(f'Digite um valor para a posição {n}: ')))
    lista.append(num)
for pos,c in enumerate(lista):
    if c == max(lista):
        pmax.append(pos)
    elif c == min(lista):
        pmin.append(pos)
print(f'Você digitou os valores {lista}')
print(f'O(s) maior(es) valor(es) foram: {max(lista)} na(s) posição(ões): {pmax}')
print(f'O(s) menor(es) valor(es) foram: {min(lista)} na(s) posição(ões): {pmin}')






