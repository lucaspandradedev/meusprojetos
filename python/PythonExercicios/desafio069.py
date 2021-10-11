maior = mulheresmenores = homem = 0
while True:
    print(20*'=')
    print('CADASTRE UMA PESSOA')
    print(20 * '=')
    i = int(input('Idade: '))
    if i > 18:
        maior += 1
    s = str(input('Sexo:[F/M]?: ')).upper()
    if s in 'M':
        homem += 1
    if s in 'F':
        if i < 20:
            mulheresmenores += 1
    print(20 * '=')
    d = str(input('Quer continuar cadastrando, [S/N]?: ')).upper()
    if d == 'N':
        break
print(f'Há {maior} pessoa(as) maiores de 18 anos, {mulheresmenores} mulher(es) com menos de 20 anos e {homem} homem(ns) cadastrados.')


