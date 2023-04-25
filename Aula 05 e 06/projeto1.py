qtd_alunos = int(input("Informe a quantidade de alunos da sala:"))
nome_alunos = []
for i in range (qtd_alunos):
    nome_alunos.append(input(f"Informe o nome do aluno: {i}"))
for x in range (i+1):
    print(nome_alunos[x], x+1)