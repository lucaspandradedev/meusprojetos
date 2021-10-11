print(40*'*' + ' TABELA BRASILEIRÃO 2021 ' + 40*'*')
tab = ('Palmeiras','Bragantino','Athletico-PR','Atlético-MG','Fortaleza','Bahia','Santos','Atlético-GO','Ceará','Corinthians','Fluminense','Flamengo','Juventude','Internacional','América-MG','São Paulo','Sport','Cuiabá','Chapecoense','Grêmio')

print(80*' ')
print(40*'*' + ' CINCO PRIMEIROS ' + 40*'*')
print(tab[0:5])
print(80*' ')
print(40*'*' + ' ULTIMOS QUATRO ' + 40*'*')
print(tab[16:20]) #pode ser [-4:0]
print(80*' ')
print(40*'*' + ' TABELA EM ORDEM ALFABÉTICA ' + 40*'*')
print(sorted(tab))
print(80*' ')
print(f'A posição ocupada pelo time da CHAPECOENSE é a {tab.index("Chapecoense")+1}ª')