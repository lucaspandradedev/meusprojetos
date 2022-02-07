from random import randint
print('Seu pc: "Irei pensar em um número entre 0 e 10...tente adivinhar!')
pc = randint(0, 10)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite?: '))
    palpites += 1
    if jogador != pc:
        print('Que pena, você errou! Tente novamente!')
    if jogador == pc:
        acertou = True
print(f'Parabéns, você acertou no {palpites}º palpite')






'''import random
palpites = 0
j = int(input('Tente adivinhar em que número pensei: '))
pc = random.randint(0, 10)
while j != pc:
    j = int(input('Que pena! Você errou! Tente novamente: '))
    palpites += 1
print(f'Seu número de tentativas foi {palpites}') está foi a minha forma de fazer'''

'''import random
j = int(input('Tente adivinhar o número no qual estou pensando, entre 0 e 5: '))
n = random.randint(0,5)
if j == n:
    print('Parabéns, você acertou!')
else:
    print('Que pena, esse não foi o número que pensei...')
    print(f'O número que pensei foi {n}')'''