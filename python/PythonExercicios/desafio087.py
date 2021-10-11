'''mat = [[],[],[]]
c1 = c2 = c3 = 1
while c1 <= 3:
    valor = int(input(f'Digite o valor [1,{c1}]: '))
    mat[0].append(valor)
    c1 += 1
while c2 <= 3:
    valor = int(input(f'Digite o valor [2,{c2}]: '))
    mat[1].append(valor)
    c2 += 1
while c3 <= 3:
    valor = int(input(f'Digite o valor [3,{c3}]: '))
    mat[2].append(valor)
    c3 += 1
print(f'[{mat[0][0]:^4}] [{mat[0][1]:^4}] [{mat[0][2]:^4}]')
print(f'[{mat[1][0]:^4}] [{mat[1][1]:^4}] [{mat[1][2]:^4}]')
print(f'[{mat[2][0]:^4}] [{mat[2][1]:^4}] [{mat[2][2]:^4}]')'''

#modo do professor abaixo
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor [{l},{c}]: '))
print(20*'-=-')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
#professor        if matriz[l][c] % 2 == 0:
#professor           somap += matriz[l][c]
    print()
print(20*'-=-')
soma = somap = 0          #foi da maneira abaixo que eu consegui fazer
for p in matriz[0]:
    if p % 2 == 0:
        somap += p
for p in matriz[1]:
    if p % 2 == 0:
        somap += p
for p in matriz[2]:
    if p % 2 == 0:
        somap += p
print(f'A soma de todos os elementos pares digitados é {somap}')
print(f'A soma dos elementos da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

'''for l in range(0, 3):
    somap += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]''' #professor

