'''listan = []
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º número: '))
    listan.append(num)
ordem = sorted(listan)
print(60*'=')
print(f'Os números digitados foram: {ordem}')
print(f'Os números pares são:', end='')
for n in ordem:
    if n % 2 == 0:
        print(f'[{n}]', end='')
print( )
print(f'Os números ímpares são:', end='')
for n in ordem:
    if n % 2 != 0:
        print(f'[{n}]',end='')
print()
print(60*'=')
print('FIM')'''

#modo do professor abaixo:
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores digitados foram {num}')
print(f'Os valores pares foram {num[0]}')
print(f'Os valores ímpares foram {num[1]}')
