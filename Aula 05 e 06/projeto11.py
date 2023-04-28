vetor_A = []
media = 0
soma = 0
cont = 0
#(1) questão
for i in range(5):
    vetor_A.append(int(input(f"Informe o número {i}")))
    soma = soma + vetor_A[i]
media = soma/5
print("")
for x in range(5):
    if vetor_A[x] % 2 == 0:
        print(f" {x}º Número par: {vetor_A[x]}")
print("")
#(2) questão
maior = vetor_A[0]
menor = vetor_A[0]
for n in range(5):
    if vetor_A[n] > maior:
        maior = vetor_A[n]
    if vetor_A[n] < menor:
        menor = vetor_A[n]
print(f"maior valor do vetor é:{maior}")
print(f"menor valor do vetor é:{menor}")
print("")
#(3) questao
for y in range(5):
    if vetor_A[y]>media:
        cont+=1
print(f"{cont} valores acima da média")