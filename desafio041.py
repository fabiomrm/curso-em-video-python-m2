#Programa que lê a data de nascimento e diz a categoria:
#até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos: juvenil
#até 20 anos: sênior
#acima: master
import datetime
ano = int(input('Digite seu ano de nascimento: '))
hoje = datetime.date.today().year
idade = hoje - ano
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUVENIL')
elif 19 < idade <=20:
    print('SÊNIOR')
else:
    print('MASTER')
