"""vetor = []
vetor2 = []
for x in range(5):
    vetor.append(float(input(f"Informe o número {x}")))
for y in range (4,-1,-1):
    vetor2.append(vetor[y])
print(vetor)
print(vetor2)"""

vetor = []
for x in range(5):
    vetor.append(float(input("Digite um número: ")))
for y in range (4,-1,-1):
    print(vetor[y])
for z in range(5):
    print(vetor[4-z])