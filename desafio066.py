#Programa que lê números inteiros e só para quando digitar 999
#mostre quantos números foram digitados e a soma (desconsiderando flag)
cont = 0
soma = 0
while True:
    num = int(input('Digite um número [para parar digite 999]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Fora digitados {cont} e a soma é {soma}')
