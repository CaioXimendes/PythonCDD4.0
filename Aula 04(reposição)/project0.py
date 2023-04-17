nota_01 = 0
nota_02 = 0
while nota_01 >= 0 and nota_01 <= 10 and nota_02 >=0 and nota_02 <=10:
    nota_01 = float(input("Olá, Informe a nota da avaliacao 01 do aluno: \n"))
    if nota_01 < 0 or nota_01 > 10:
        print("Os valores da nota devem estar entre 0 em 10! Tente novamente!")
        break
    nota_02 = float(input("Olá, Informe a nota da avaliacao 02 do aluno: \n"))
    if nota_02 < 0 or nota_02 > 10:
        print("Os valores da nota devem estar entre 0 em 10! Tente novamente!")
        break
    media = (nota_01 + nota_02) / 2
    print("A média do aluno foi :", media)