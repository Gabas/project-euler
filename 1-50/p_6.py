'''
    Problema 6: diferença de somatório dos quadrados

1^2 + 2^2 + 3^2 ... + 10^2 = 385
(1+2+3... + 10)^2 = 55^2 = 3025

3025 - 385 = 2640


'''

REPETICOES = 101
somatorio_quadrados = 0
quadrado_somatorios = 0

for i in range(REPETICOES):
    somatorio_quadrados += i**2 

for i in range(REPETICOES):
    quadrado_somatorios += i

quadrado_somatorios = quadrado_somatorios**2

print(quadrado_somatorios-somatorio_quadrados)