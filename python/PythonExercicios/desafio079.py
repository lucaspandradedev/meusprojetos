lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Esse número já foi digitado, por favor digite outro!')
    r = str(input('Deseja continuar [S/N]?: ')).upper()
    if r == 'N':
        break
print(40*'=')
print(f'Você digitou os números {sorted(lista)}')