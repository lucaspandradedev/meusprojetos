soma = 0
c = 0
qt = 0
d = 's'
while d in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    d = str(input('Deseja continuar [S/N]: '))
print(f'O média entre os números é {soma/c}')
print(f'O maior entre eles é {maior} e o menor {menor}')
