vetor_A = []
vetor_M = []
for x in range(10):
    vetor_A.append(float(input(f"Informe o número {x}\n")))
x = int(input("Informe o multiplicador: \n"))
for i in range(10):
    vetor_M.append(vetor_A[i]*x)
print(f"O vetor A é : {vetor_A}")
print(f"O multiplicador é igual a {x}")
print(f"O vetor M é : {vetor_M}")