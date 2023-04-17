nome= input("Olá! Digite o seu nome: \n")
idade= input(f"{nome}, Qual a sua idade?\n")
salario= float(input(f"{nome}, Informe o seu salário:\n"))
percentual_aumento= float(input("Informe o percentual de aumento do salário: (ex: 50) \n"))
salario_aumento= (salario*percentual_aumento/100)+salario
print(f"{nome}, seus dados são:\n Nome: {nome}\n Idade: {idade} anos\n Salário:R$ {salario}\n Salário com aumento: R$ {salario_aumento}")