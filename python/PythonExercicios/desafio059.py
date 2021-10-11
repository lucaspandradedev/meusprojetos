from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = 0
while op != 5:
    print('[1] somar', '[2] multiplicar', '[3] maior', '[4] novos números', '[5] sair do programa')
    op = int(input('Qual operação deseja realizar?: '))
    if op == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif op == 2:
        produto = n1 * n2
        print(f'O produto entre {n1} e {n2} é {produto}')
    elif op == 3:
        if n1 > n2:
            print(f'O maior número é o {n1}')
        if n1 < n2:
            print(f'O maior número é o {n2}')
    elif op == 4:
        print('Quais números deseja?')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('O opção inválida, por favor tente uma das possíveis.')
sleep(1)
print('Fim do programa, volte sempre!')



















'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('[1] somar', '[2] multiplicar', '[3] maior', '[4] novos números', '[5] sair do programa')
op = int(input('Qual operação você deseja? '))
dec = 0
while op != 5:
    while dec != 's':
        if op == 1:
            print(f'A soma entre {n1} e {n2} é {n1 + n2}')
            dec = str(input('Deseja reiniciar o programa, [s/n]? '))
            if dec == 'n':
                print('Obrigado!')
            if dec == 's':
                n1 = int(input('Digite um novo número: '))
                n2 = int(input('Digite outro número: '))
                op = int(input('Qual operação deseja realizar?: '))
        if op == 2:
            print(f'A soma entre {n1} e {n2} é {n1 * n2}')
            dec = str(input('Deseja reiniciar o programa, [s/n]? '))
            if dec == 'n':
                print('Obrigado!')
            if dec == 's':
                n1 = int(input('Digite um novo número: '))
                n2 = int(input('Digite outro número: '))
                op = int(input('Qual operação deseja realizar?: '))
        if op == 3:
            if n1 > n2:
                print(f'O maior entre estes dois números é {n1}')
            if n1 < n2:
                print(f'O maior entre estes dois números é {n2}')
                dec = str(input('Deseja reiniciar o programa, [s/n]? '))
                if dec == 'n':
                    print('Obrigado!')
                if dec == 's':
                    n1 = int(input('Digite um novo número: '))
                    n2 = int(input('Digite outro número: '))
                    op = int(input('Qual operação deseja realizar?: '))
        if op == 4:
            n1 = int(input('Digite um novo número: '))
            n2 = int(input('Digite outro número: '))
            op = int(input('Qual operação deseja realizar?: '))
            dec = str(input('Deseja reiniciar o programa, [s/n]? '))
            if dec == 'n':
                print('Obrigado!')'''





'''if op == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    if op == 2:
        print(f'O produto entre {n1} e {n2} é {n1 * n2}')
    if op == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
        elif n1 < n2:
            print(f'O maior número entre {n1} e {n2} é {n2}')
    if op == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite um outro número: '))
        op = int(input('Qual operação deseja fazer com esses novos números?: '))
        if op == 1:
            print(f'A soma entre {n1} e {n2} é {n1 + n2}')
        if op == 2:
            print(f'O produto entre {n1} e {n2} é {n1 * n2}')'''
