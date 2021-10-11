c = n = soma = 0
while n != 999:                              # posso fazer com while true
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'Você digitou {c} números e a soma deles é {soma}')         # para colorir \033[1;4;32m
