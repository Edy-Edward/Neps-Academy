#Essa linha de código permite que o programa leia dois valores inteiros fornecidos pelo usuário em uma única linha, separados por espaço, e os armazene nas variáveis A e B.
p, r = map(int, input().split())



#Saída
if p == 0:
    print("C")
else: 
    if r == 0:
        print("B")
    else:
        print("A")