#Programa que lê 06 números inteiros e mostra soma dos que forem par e desconsidera os ímpares
s = 0
for c in range(0,6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s = s + n
print(f'A soma dos números pares escolhidos é: {s}')
