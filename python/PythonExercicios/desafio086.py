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
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()





