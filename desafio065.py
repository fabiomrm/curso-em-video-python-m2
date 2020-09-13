#Programa que lê vários números inteiros. No final ele mostra:
#Média entre os valores, o maior e o menor.
#Programa pergunta se ele quer continuar a digitar valores.
pergunta = 'SIM'
cont = 0
soma = 0
maior = 0
menor = 0
while pergunta == 'SIM':
    num = int(input('Digite um número: '))
    soma = soma + num
    cont = cont + 1
    pergunta = str(input('Deseja digitar outro valor? ')).strip().upper()
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
média = soma/cont
print(soma)
print(cont)
print(f'A média de valores é {média}')
print(f'O maior número digitado foi: {maior}, o menor foi {menor}')