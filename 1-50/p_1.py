'''
    Problema 1: somatório dos múltiplos de 3 e 5 menores que 1000
'''

soma = 0

for i in range (1000):
    if ((i % 3) == 0) or ((i % 5) == 0):
        soma += i

print(soma)