#Programa que joga par ou ímpar e só para quando o jogador perder
#mostra a quantidade de vitórias consecutivas
from random import randint
cont = 0
while True:
    num_pc = randint(0, 11)
    print(num_pc)
    num = int(input('Digite um número: '))
    opc = str(input('Par ou ímpar? ')).strip().upper()
    total = num_pc + num
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    if resultado == opc:
        print(f'Você VENCEU! {total} é {resultado}! Vamos novamente:')
    else:
        break
    cont = cont + 1
print(f'Você PERDEU! {total} é {resultado} Sua sequência foi de {cont} vitórias.')







