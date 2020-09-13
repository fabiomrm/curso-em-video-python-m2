#Programa que lê duas notas e diz a média
#abaixo de 5.0 -> Reprovado
#entre 5.0 e 6.9 -> Recuperação
#7.0 ou mais -> Aprovado
n1 = float(input('Primeira nota: '))
n2 = float(input('Primeira nota: '))
media = float((n1 + n2) / 2)
print(media)
if media < 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')