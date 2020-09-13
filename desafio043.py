#Programa que calcula IMC e diz:
#Abaixo de 18.5: Abaixo do peso
#18.5 a 25: Peso ideal
#25 a 30: Sobrepeso
#30 a 40: Obesidade
#acima de 40: Obesidade mórbida
print(str('\033[1;35mCÁLCULO DO IMC\033[m'))
peso = float(input('Qual o seu peso (em kg)? '))
altura = float(input('Qual é a sua altura (em metros)? '))
imc = float(peso / (altura ** 2))
print(f'Seu IMC atual é: {imc:.1f}')
if imc < 18.5:
    print ('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print ('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('ATENÇÃO! Obesidade!')
else:
    print('ATENÇÃO! Obesidade mórbida!')
