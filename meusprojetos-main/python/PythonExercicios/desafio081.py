lista = []
while True:
    n = int(input('Digite un número: '))
    lista.append(n)
    r = str(input('Deseja continuar [S/N]?: ')).strip().upper()
    if r not in 'SN':
        print('Dígito errado! Responda S ou N!')
        r = str(input('Deseja continuar [S/N]?: ')).strip().upper()
    if r == 'N':
        break
print(50*'=')
print(f'Os número digitados foram {lista}')
print(f'Ao todo foram {len(lista)} números digitados')
lista.sort(reverse=True)
print(f'A ordem decrescente para essa lista é {lista}')
if 5 in lista:
    print('O número 5 foi digitado e está presente na lista')
else:
    print('O número 5 não foi digitado')