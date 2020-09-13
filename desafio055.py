#Programa que lê 05 pesos e diz o maior e menor
for c in range(0,5):
    peso = float(input('Digite o peso: '))
    if c == 0:
        peso1 = peso
    elif c == 1:
        peso2 = peso
    elif c == 2:
        peso3 = peso
    elif c == 3:
        peso4 = peso
    else:
        peso5 = peso
pesos = [peso1, peso2, peso3, peso4, peso5]
print(f'Dos pesos informados, o maior é \033[4;33m{max(pesos)}\033[m kgs e o menor é \033[4;33m{min(pesos)}\033[m kgs')







