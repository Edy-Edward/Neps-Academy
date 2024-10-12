# Lendo a entrada do exercício
B = int(input())
C = int(input())


total = B + C

"""O resto da divisão por dois da variável 'total'
é o que determina se um número é par ou ímpar"""
if total % 2 == 0:
    print("Bino")

else:
    print("Cino")