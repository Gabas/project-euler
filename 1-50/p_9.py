"""
    Problema 8: produto do triângulo pitagórico em que a+b+c = 1000
"""

def produto_triangulo():
    for m in range(2, 100):
        for n in range(1, m):
            #fórmula para gerar ternas de triângulos pitagóricos
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2

            soma = a + b + c

            if 1000 % soma == 0:
                k = 1000 // soma 
                a *= k
                b *= k
                c *= k
                return (a * b * c)

produto = produto_triangulo()
print(produto)