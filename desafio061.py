#Refazer o desafio 51 usando WHILE
#Lê o primeiro termo e a razão da PA e mostra os 10 primeiros termos
termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo_quantidade = int(input('Quantos termos você quer ver? '))
cont = 0
while cont < termo_quantidade:
    termo = termo1 + razao*cont
    cont = cont + 1
    print(termo, end=' ')

