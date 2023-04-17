nota_1 = float(input("Olá! Digite a nota 01 do aluno: \n"))
nota_2 = float(input("Olá! Digite a nota 02 do aluno: \n"))
nota_3 = float(input("Olá! Digite a nota 03 do aluno: \n"))
media = (nota_1+nota_2+nota_3)/3
if media >= 7:
    print("Aluno Aprovado")
else:
    if media>=4:
       print("Aluno em recuperação")
    else:
        print("Reprovado")