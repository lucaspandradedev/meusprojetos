lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    re = str(input('Deseja continuar [S/N]?: ')).upper().strip()
    if re not in 'SN':
        print('Resposta inválida, tente novamente!')
        re = str(input('Deseja continuar [S/N]?: ')).upper().strip()
    if re == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os valores digitados são {lista}')
print(f'Os valroes pares são {pares}')
print(f'Os valores ímpares são {impares}')
