#A, B = map(float, input().split())

A, B = input().split()

A = float(A)
B = float(B)

media = (A+B) / 2
resposta = ''

if media >= 7:
    resposta = 'Aprovado'

elif media < 7 and media >= 4:
    resposta = 'Reprovado'

else:
    resposta = 'Recuperação'

print(resposta)