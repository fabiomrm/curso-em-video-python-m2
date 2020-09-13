#Programa que faça contagem regressiva de 10 segs para explosão de fogos de artifício
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;32mFELIZ ANO NOVO!\033[m')
