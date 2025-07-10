'''
    Problema 4: maior palíndromo feito a partir do produto de dois números com 3 algarismos
'''

pali = 10
maior = 0
i = 999
j = 999

def check_palindromo(p):
    p = str(p)
    if (p == p[::-1]):
        return True
    
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        pali = i*j
        if (check_palindromo(pali)) and (pali>maior):
            maior = pali

print(maior)            