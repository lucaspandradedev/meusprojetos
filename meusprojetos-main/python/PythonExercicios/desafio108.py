import moedas

v = float(input('Digite o preço R$: '))
print(f'Aumentando 14%, temos {moedas.aumentar(v,14,True)}')
print(f'Diminuindo 14%, temos {moedas.diminuir(v,14,True)}')
print(f'O dobro de {moedas.moeda(v)} é {moedas.dobro(v,True)}')
print(f'A metade de {moedas.moeda(v)} é {moedas.metade(v,True)}')

