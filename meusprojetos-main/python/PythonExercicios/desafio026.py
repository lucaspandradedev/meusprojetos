n = str(input('Digite uma frase: ')).strip()
c = n.count('a')
fa = n.find('a')
la = len(n)-n[::-1].find('a')
print(f'A letra "a" aparece {c} vezes')
print(f'A letra "a" aparece a primeira vez na posição {fa+1}')
print(f'A letra "a" aparece a última vez na posição {la}')
print(n[::-1])
'''também posso acrescentar +1 na contagem de "fa" para que a posição fique mais natural ao nosso modo de contar'''
'''o professor utilizou, para encontrar a ultima ocorrencia da letra "a", a função "rfind"! assim fica facil'''