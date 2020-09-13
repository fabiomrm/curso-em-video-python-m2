#Programa que lê quantos são maior de idade e quantos são menor de idade
import datetime
maior_de_idade = 0
menor_de_idade = 0
for c in range(0, 4):
    ano = int(input('Digite o ano de nascimento: '))
    if (datetime.date.today().year - ano) > 21:
        maior_de_idade = maior_de_idade + 1
    else:
        menor_de_idade = menor_de_idade + 1
print(f'Maior de idade: {maior_de_idade}\nMenor de idade: {menor_de_idade}')
