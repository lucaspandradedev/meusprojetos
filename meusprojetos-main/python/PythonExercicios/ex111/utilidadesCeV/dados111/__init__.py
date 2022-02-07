def leiaDinheiro(txt):
    valido = False
    while not valido:
        resp = str(input(txt)).strip().replace(',','.')
        if resp.isalpha():
            print(f'\033[1:31mERRO! "{resp}" não é um preço válido''\033[m')
        else:
            valido = True
            respv = float(resp)
            v = respv
            return v

