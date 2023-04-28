vetor_A = []
vetor_B = []
vetor_C = []

for i in range(5):
    vetor_A.append(float(input(f"Informe o número {i} do vetor A ")))
for x in range(5):
    vetor_B.append(float(input(f"Informe o número {x} do vetor B ")))
for y in range(5):
    vetor_C.append(vetor_A[y]+vetor_B[y])
print(vetor_C)