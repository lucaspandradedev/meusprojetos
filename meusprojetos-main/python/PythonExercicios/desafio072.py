n = int(input('Digite um número entre 0 e 20: '))
extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','des','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
nome = n
while n < 0 or n > 20:
    n = int(input('O número que você digitou não está dentro da janela. Tente novamente: '))
print(f'Você digitou o número {extenso[n]}')
print('OBRIGADO!')
#n = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','des','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
