import random
print('=-='*20)
print(' '*15 + '\033[1;4;7;37;40m VAMOS JOGAR JOKENPÔ?!\033[m')
j = input('Qual você escolhe pedra, papél ou tesoura?: ')
c = random.randint(1,3)
if j == 'pedra' and c == 3:
    print('EU ESCOLHI TESOURA')
    print('PARABÉNS, VOCÊ ME VENCEU!')
elif j == 'pedra' and c == 2:
    print('EU ESCOLHI PAPÉL')
    print('QUE PENA...VOCÊ PERDEU')
elif j == 'pedra' and c == 1:
    print('EU ESCOLHI PEDRA')
    print('NÓS EMPATAMOS!')
elif j == 'papél' and c == 3:
    print('EU ESCOLHI TESOURA')
    print('QUE PENA... VOCÊ PERDEU!')
elif j == 'papél' and c == 2:
    print('EU ESCOLHI PAPÉL')
    print('NÓS EMPATAMOS!')
elif j == 'papél' and c == 1:
    print('EU ESCOLHI PEDRA')
    print('PARABÉNS, VOCÊ ME VENCEU')
elif j == 'tesoura' and c == 1:
    print('EU ESCOLHI PEDRA')
    print('QUE PENA...VOCÊ PERDEU!')
elif j == 'tesoura' and c == 2:
    print('EU ESCOLHI PAPÉL')
    print('PARABÉNS, VOCÊ ME VENCEU!')
elif j == 'tesoura' and c == 3:
    print('EU ESCOLHI TESOURA')
    print('NÓS EMPATAMOS!')
print(' '*15 + '\033[1;4;7;37;40m OBRIGADO POR JOGAR COMIGO!\033[m')
print('=-='*20)

''''resposta do professor
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('O computador escolheu {}'.format(itens[computador])''''''