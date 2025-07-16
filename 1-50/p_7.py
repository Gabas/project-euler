'''
    Problema 7: o 10001 número primo
'''

n = 2
QTD_PRIMOS = 0

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


while (QTD_PRIMOS < 10001):
    if is_primo(n):
        QTD_PRIMOS += 1

    if (QTD_PRIMOS == 10001):
        break

    n += 1

print(n)

#print(n)
#print(QTD_PRIMOS)