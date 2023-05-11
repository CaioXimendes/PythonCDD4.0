pergunta = "s"
while pergunta == "s":
    num = float(input("Digite um número: "))
    if num != 0:
        if num > 0:
            print("Este número é maior que zero ou positivo")
        else:
            print("Este número é menor que zero ou negativo")
    else:
        print("número igual a zero")
    pergunta = input("Deseja continuar? s/n")
else:
    print("Fim do programa!")