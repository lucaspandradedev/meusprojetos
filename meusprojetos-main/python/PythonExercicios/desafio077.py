dic = ('phyton','maça','mel','bola','elefante','curso','programação','guanabara','cursoemvideo')
for p in dic:
    print(f'\nNa palavra {p.upper()} temos:', end='')
    for vogal in p:
        if vogal in 'aeiou':
            print(vogal, end=' ')
