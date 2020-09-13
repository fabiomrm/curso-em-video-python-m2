#Lê um número inteiro e diz se ele é primo ou não
import math
num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[31m{c}\033[m', end=' ')
        tot = tot + 1
    else:
        print(c, end=' ')
if tot == 2:
    print(f'\nO número {num} \033[32mé\033[m primo')
else:
    print(f'\nO número {num}\033[33m não é\033[m primo ')























