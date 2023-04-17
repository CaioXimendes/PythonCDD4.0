#Faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo valor recebido
#caso o segundo valor digitado, seja zero, solicite novamente o valor, informando que só aceitaremos
#valores diferentes de zero.
divisao = 0
num_1 = float(input("Digite o número 01: \n"))
num_2 = float(input("Digite o número 02: \n"))
while num_2 == 0:
    num_2 = float(input("O número 02 deve ser diferente de zero! informe o valor do número 02 novamente: \n"))
else:
    divisao = num_1/num_2
    print(f"A divisão do número 01 pelo número 02 foi: {divisao}")