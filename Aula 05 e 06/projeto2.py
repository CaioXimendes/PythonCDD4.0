qtd_alunos = int(input("Informe a quantidade de alunos da sala:"))
nome_alunos = []
cont = 0
for i in range (qtd_alunos):
    nome_alunos.append(input(f"Informe o nome do aluno: {i}"))
nome_pesquisa = input("Informe o nome do aluno para pesquisar: \n")
for x in range(qtd_alunos):
    if nome_pesquisa == nome_alunos[x]:
        print(nome_alunos[x], x)
    else:
        cont += 1
if cont == qtd_alunos:
    print("Nome não encontrado!")