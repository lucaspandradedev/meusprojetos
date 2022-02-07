def notas(*num, sit=False):
    """
    -> Função para analisar as notas e a situação de um aluno
    :param num: São as notas do aluno
    :param sit: É a situação do aluno de acordo com a média (para mostrar, mude esse parâmetro para True)
    :return: Mostra as informações do aluno
    """
    print(30*'-=')
    resp = {}
    resp['Total'] = len(num)
    resp['Maior'] = max(num)
    resp['Menor'] = min(num)
    resp['Média'] = (sum(num)/len(num))
    if sit:
        if resp['Média'] < 6:
            resp['Situação'] = 'Ruim'
        elif 6 <= resp['Média'] < 7:
            resp['Situação'] = 'Regular'
        else:
            resp['Situação'] = 'Ótima!'
    return resp


resp = notas(8, 5.5, 10, 7, sit=False)
print(resp)
help(notas)