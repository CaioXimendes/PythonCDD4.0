operacao = 0
resultado = 0
num_01 = float(input("Digite o primeiro número: \n"))
num_02 = float(input("Digite o segundo número: \n"))
while operacao != 6:
    operacao = int(input("1. para soma:\n"
                         "2. para subtracao:\n"
                         "3. para multiplicação:\n"
                         "4. para divisão:\n"
                         "5. para para digitar um novo número:\n"
                         "6. para sair:\n"))
    while True:
        if operacao == 1:
            resultado = num_01+num_02
            print(f"O resultado foi: {resultado}")
            break
        elif operacao == 2:
            resultado = num_01-num_02
            print(f"O resultado foi: {resultado}")
            break
        elif operacao == 3:
            resultado = num_01*num_02
            print(f"O resultado foi: {resultado}")
            break
        elif operacao == 4:
            resultado = num_01/num_02
            print(f"O resultado foi: {resultado}")
            break
        elif operacao == 5:
            num_01 = float(input("Digite o primeiro número: \n"))
            num_02 = float(input("Digite o segundo número: \n"))
            break
        elif operacao == 6:
            print("fim do programa!")
            break
