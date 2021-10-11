a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))
ab1 = abs(b-c)
ab2 = abs(a-c)
ab3 = abs(a-b)
if ab1<a<b+c or ab2<b<a+c or ab3<c<a+b:
    print('As retas formam um triângulo')
    if a == b and b == c:
        print('E esse triângulo é \033[1;7;46m Equilátero \033[m')
    elif a != b != c:
        print('E esse triângulo é \033[1;7;46m Escaleno \033[m')
    else:
        print('E esse triângulo é \033[1;7;46m Isósceles \033[m')
else:
    print('As retas não formam um triângulo!')
#if ab2<b<a+c:
    #print('As retas formam um triângulo')
#if ab3<c<a+b:
    #print('As retas formam um triângulo')
