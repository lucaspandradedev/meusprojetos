from desafio115.lib import *
from desafio115.lib.arquivo import *
from time import sleep

arq = 'cadastroslucas.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

# professor Guanabara fez: resposta = menu([opc1, opc2, opc3, etc])
while True:
    head('MENU PRINCIPAL')
    num = opc()
    if num == 1:
        lerArquivo(arq)
        sleep(2)
    elif num == 2:
        opc1('Cadastrar novas pessoas')
        sleep(2)
    elif num == 3:
        opc1('SAINDO DO SISTEMA...ATÉ LOGO!')
        break