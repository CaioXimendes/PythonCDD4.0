numero = int(input("Digite o numero correspondente ao mês, Entre 1 e 12: \n"))
if numero >= 1 and numero <= 12:
    if numero == 1:
        print("Mês de janeiro")
    elif numero == 2:
        print("Mês de Fevereiro")
    elif numero == 3:
        print("Mês de Março")
    elif numero == 4:
        print("Mês de Abril")
    elif numero == 5:
        print("Mês de Maio")
    elif numero == 6:
        print("Mês de Junho")
    elif numero == 7:
        print("Mês de Julho")
    elif numero == 8:
        print("Mês de Agosto")
    elif numero == 9:
        print("Mês de Setembro")
    elif numero == 10:
        print("Mês de Outubro")
    elif numero == 11:
        print("Mês de Novembro")
    else:
        print("Mês de Dezembro")
else:
    print("Número incorreto! Este mês não existe!!")
