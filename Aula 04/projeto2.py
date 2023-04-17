i = 1
num_alunos = int(input("Informe a quantidade de alunos: \n"))
soma_alunos = 0
while i <= num_alunos:
    notas_alunos = float(input(f"Digite a nota do aluno {i} \n"))
    soma_alunos += notas_alunos
    #soma_alunos = notas_alunos + soma_alunos
    i += 1
    #i = i + 1
print(f"A média dos alunos da turma foi: {soma_alunos/num_alunos}")
#ou posso fazer também print(f"A média dos alunos da turma foi: {soma_alunos/(i-1)} mas a logica estaria errada.")