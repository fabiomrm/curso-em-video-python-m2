#Desafio 35 agora dizendo se o triângulo é escaleno, isósceles ou equilátero
from math import fabs
n1 = float(input('Segmento r1: '))
n2 = float(input('Segmento r2: '))
n3 = float(input('Segmento r3: '))
if (fabs(n2 - n3) < n1 < (n2 + n3)) \
and (fabs(n1 - n3) < n2 < (n1 + n3)) \
and (fabs(n1 - n2) < n3 < (n1 + n2)):
    if n1 != n2 != n3 != n1:
        print('Essas retas formam um triângulo \033[1;31;42mESCALENO\033[m')
    elif n1 == n2 == n3:
        print('Essas retas formam um triângulo \033[1;31;42mEQUILÁTERO\033[m')
    else:
        print('Essas retas formam um triângulo \033[1;31;42mISÓSCELES\033[m')
else:
    print(str('\033[4;31;47mEssas retas não formam um triângulo\033[m').upper())
