#Programa que aprova empréstimo bancário.
#Ele vai perguntar: valor da casa, salário e quantos anos ele vai pagar
#Vai calcular o valor da prestação e se ele vai ou não poder comprar a casa
#O valor da parcela não vai poder ser maior que 30% do salário
valor_imovel = float(input('Digite o valor do imóvel: R$ '))
valor_salario = float(input('Digite o valor do salário: R$ '))
tempo_ano = int(input('Em quantos anos pretende pagar? '))
tempo_mes = int(tempo_ano * 12)
prestacao = float(valor_imovel / tempo_mes)
print(f'Essa simulação retorna uma prestação mensal de: R$ {prestacao:.2f}')
if prestacao > (valor_salario * 0.3):
    print(f'O valor da prestação R$ {prestacao:.2f} ultrapassa o limite de 30% do salario.\n\033[4;31mCRÉDITO REPROVADO\033[m')
else:
    print(f'O valor da prestação R$ {prestacao:.2f} está dentro do limite de 30% do salário.\n\033[4;32mCRÉDITO APROVADO\033[m')


