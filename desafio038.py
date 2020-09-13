#Programa que lê dois números inteiros e diz qual é maior ou se são iguais
import math
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O maior número é \033[1;30;41m{n1}\033[m')
elif n2 > n1:
    print(f'O maior número é \033[1;30;41m{n2}\033[m')
else:
    print('\033[4;31;33mOs números são iguais!\033[m')
