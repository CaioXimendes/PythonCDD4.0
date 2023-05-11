pergunta = "s"
vetor_media = []
cont = 0
while pergunta != "n":
    nota_1 = float(input("Digite a nota 01:"))
    nota_2 = float(input("Digite a nota 02:"))
    media = (nota_1 + nota_2) / 2
    vetor_media.append(media)
    if media >= 7:
        print("Aluno Aprovado:")
    elif media >= 4:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado!")
    pergunta = input("você deseja continuar? s/n")
    cont+=1
else:
    print(f"media dos alunos foram: {vetor_media}")
for x in range(cont):
    print(vetor_media[x], end = "")