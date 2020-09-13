#Simula um funcionamento de caixa eletrônico
#Pergunta o valor a ser sacado e ele informa quantas cédulas de cada valor serão entregues
#Considerar cédulas de 50, 20, 10 e 1
print('CAIXA ELETRÔNICO')
valor = int(input('Digite o valor que deseja sacar: R$ '))
#Quantidade de cédulas de 50:
ced_50 = valor // 50
print(ced_50)
#Quantidade de cédulas 20:
ced_20 = (valor % 50) // 20
print(ced_20)
#Quantidade de cédulas de 10:
ced_10 = (valor % 20) // 10
print(ced_10)
#Quantidade de cédulas de 1:
ced_1 = (valor % 10) // 1
print(ced_1)

