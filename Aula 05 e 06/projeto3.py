notas_alunos = []
soma = 0
cont = 0
for x in range (5):
    notas_alunos.append(float(input(f"Informe a nota do aluno {x}")))
for n in range(5):
    soma += notas_alunos[n]
media = soma/5
for y in range(5):
    if notas_alunos[y] >= media:
        cont+=1
print(f"{cont} alunos foram aprovados e a média da turma foi: {media}")