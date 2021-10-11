import random
j = int(input('Tente adivinhar o número no qual estou pensando, entre 0 e 5: '))
n = random.randint(0,5)
if j == n:
    print('Parabéns, você acertou!')
else:
    print('Que pena, esse não foi o número que pensei...')
    print(f'O número que pensei foi {n}')

'''o professor utilizou a função sleep, importada do módulo time'''