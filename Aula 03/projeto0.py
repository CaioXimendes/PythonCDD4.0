numero_1= float(input("Digite o número 01: \n"))
numero_2= float(input("Digite o número 02: \n"))
if numero_1 != numero_2:

    if numero_1 > numero_2:
        print(numero_2)
        print(numero_1)
    else:
        print(numero_1)
        print(numero_2)
if numero_1 == numero_2:
    print("O número 01 não pode ser igual ao número 02")