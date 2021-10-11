from random import randint
print('VAMOS JOGAR PAR OU IMPAR!')
cv = 0
pi = 'pi'
while True:
    print(20*'=-')
    j = int(input('Digite um número: '))
    pi = str(input('Você escolhe par ou impar, [P/I]?: ')).upper()
    while not pi in 'PI':
        pi = str(input('Você escolhe par ou impar, [P/I]?: ')).upper()
    pc = randint(0, 10)
    p = (j+pc)
    if pi == 'P':
        if p % 2 == 0:
            print(f'Você escolheu {j} e o computador jogou {pc}, o resultado deu {j+pc}, que é PAR')
            print('PARABÉNS, VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            cv += 1
        else:
            print(f'Você escolheu {j} e o computador jogou {pc}, o resultado deu {j + pc}, que é IMPAR')
            print(f'GAME OVER! Você venceu {cv} vez(s)')
            break
    if pi == 'I':
        if p % 2 != 0:
            print(f'Você escolheu {j} e o computador jogou {pc}, o resultado deu {j+pc}, que é IMPAR')
            print('PARABÉNS, VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            cv += 1
        else:
            print(f'Você escolheu {j} e o computador jogou {pc}, o resultado deu {j + pc}, que é PAR')
            print(f'GAME OVER! Você venceu {cv} vez(s)')
            break




