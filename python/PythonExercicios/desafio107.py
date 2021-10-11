import moedas

v = float(input('Digite o preço R$: '))
print(f'Aumentando 14%, temos {moedas.aumentar(v,14)}')
print(f'Diminuindo 14%, temos {moedas.diminuir(v,14)}')
print(f'O dobro de {v} é {moedas.dobro(v)}')
print(f'A metade de {v} é {moedas.metade(v)}')
