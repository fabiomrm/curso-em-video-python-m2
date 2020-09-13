#Programa que pede número N e mostra os N primeiros números da seq de Fibonacci
num = int(input('Digite a quantidade de números que deseja saber: '))
t1 = 0
t2 = 1
print(t1, end=' ')
print(t2, end=' ')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    cont += 1






