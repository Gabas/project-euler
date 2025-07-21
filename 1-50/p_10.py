"""
    Problema 10: somatório dos primos menores que 2000000
"""

def is_primo(n):
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if (n % 2 == 0):
        return False

    divisor = 3
    
    while divisor**2 <= n:
        if n % divisor == 0:
            return False
        divisor += 2

    return True

somatorio = 0

for i in range(2000000):
    if (is_primo(i)):
        somatorio += i

print(somatorio)

# Ideia: fazer uma biblioteca de funções genéricas, tendo em vista que este exercício foi apenas uma repetição do exercício 7