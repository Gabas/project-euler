'''
    Problema 3: maior fator primo de 600851475143
'''

num = 600851475143

fator = 2
while fator * fator <= num:
    if num % fator == 0:
        num //= fator  
    else:
        fator += 1 

print (num)