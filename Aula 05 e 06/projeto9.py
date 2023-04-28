vetor_A = []
cont = 0
for i in range(5):
    vetor_A.append(float(input(f"Informe o número {i} do vetor A: ")))
b = float(input("Informe o número contido no vetor A: "))
for x in range(5):
    if b == vetor_A[x]:
        cont+=1
print(f"O número {b} aparece {cont} vezes no vetor A")