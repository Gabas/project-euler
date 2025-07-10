'''
    Problema 2: somatório dos números de Fibonacci pares menores que 4000000
'''

n1 = 1
n2 = 1
fibo = n1
soma = 0

while (fibo < 4000000):
    if (fibo % 2 == 0):
        soma += fibo

    fibo = n1+n2
    n1 = n2
    n2 = fibo

print(soma)