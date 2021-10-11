print(40 * '-')
print(5*' ', 'SUPER MERCADINHO DO ANDRADE')
print(40 * '-')
cp = soma = menor = c = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do produto R$: '))
    soma += preço
    c += 1
    if preço > 1000:
        cp += 1
    if c == 1 or preço < menor:
        menor = preço
        barato = nome
    d = str(input('Quer continuar comprando [S/N]? ')).upper()
    if d == 'N':
        break
print(f'{cp} itens custaram mais de 1000 R$')
print(f'A soma dos preços dos produtos foi {soma} R$')
print(f'O produto mais barato foi {barato} e custou {menor} R$')