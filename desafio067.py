#Programa que mostra a tabuada de vários números, um de cada vez, e para quando o número for negativo

while True:
    cont = 0
    num = int(input('Quer ver a tabuada de qual valor? [Para interromper digite número negativo] '))
    if num < 1:
        break
    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont = cont + 1
print('FIM')

