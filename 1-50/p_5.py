'''
    Problema 5: menor número divisível pelos números de 1 a 20
'''

num = 1

def check_divisivel(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True
            
n = 20

# check_divisivel(2520)

while not check_divisivel(n):
    n += 20

print(n)