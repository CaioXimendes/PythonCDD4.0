nota_01 = 0
nota_02 = 0
pergunta = "S"
while pergunta == "S":
    nota_01 = float(input("Olá, Informe a nota da avaliacao 01 do aluno: \n"))
    while nota_01 < 0 and nota_01 > 10:
        print("Os valores da nota devem estar entre 0 em 10! Tente novamente!")
    nota_02 = float(input("Olá, Informe a nota da avaliacao 02 do aluno: \n"))
    while nota_02 < 0 and nota_02 > 10:
        print("Os valores da nota devem estar entre 0 em 10! Tente novamente!")
    media = (nota_01 + nota_02) / 2
    print("A média do aluno foi :", media)
    pergunta = input("Deseja continuar? S/N para Sim ou Não \n")
else:
    print("Fim do programa!")