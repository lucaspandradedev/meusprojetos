n = 0
soma = 0
qt = 0
while n != 999:
    n = int(input('Digite um número qualquer; se quiser parar, digite 999: '))
    soma += n
    qt += 1
qt2 = qt - 1
soma2 = soma - 999
print(f'Você digitou {qt2} números e a soma entre eles foi {soma2}')

''' modo do professor n = c = soma = 0
n = int(input('Digite um número qualquer. Se quiser sair, digite 999: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número qualquer. Se quiser sair, digite 999: '))
print(f'Você digitou {c} números e e soma entre eles deu {soma}')'''