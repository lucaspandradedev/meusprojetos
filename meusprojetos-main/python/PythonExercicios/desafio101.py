def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if 18 <= idade < 65:
        return f'Com {idade} anos: \033[1;31m''VOTO OBRIGATÓRIO''\033[m'
    elif idade < 18:
        return f'Com {idade} anos: \033[1;34m''NÃO VOTA''\033[m'
    else:
        return f'Com {idade} anos: \033[1;32m''VOTO FACULTATIVO''\033[m'


print(30*'=')
ano = int(input('Em que ano você nasceu?: '))
print(voto(ano))