#Programa que lê vários números inteiros e para quando digita 999
#Mostra quantos números foram digitados e a soma
num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número. Digite 999 para parar'))
    if num != 999:
        cont = cont + 1
        soma = soma + num
print(f'Foram digitados {cont} números. A soma deles é {soma}')


