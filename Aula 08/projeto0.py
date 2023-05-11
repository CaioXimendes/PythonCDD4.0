def somar(n1,n2):
    soma = n1 + n2
    print(f"A soma foi: {soma}")
def subtrair(n1,n2):
    subtracao = n1 - n2
    print(f"A subtração foi: {subtracao}")
def multiplicar(n1,n2):
    mult = n1 * n2
    print(f"A multiplicação foi: {mult}")
def dividir(n1,n2):
    divisao = n1 / n2
    print(f"A divisão foi: {divisao}")

pergunta = 0
while pergunta != 5:
    pergunta = int(input("1 - somar\n"
                         "2 - subtrair\n"
                         "3 - multiplicar\n"
                         "4 - dividir\n"
                         "5 - sair\n"))
    if pergunta == 5:
        print("Fim da calculadora!")
        break
    n1 = float(input("Informe um número: "))
    n2 = float(input("Informe outro número: "))
    match pergunta:
        case 1:
            somar(n1,n2)
        case 2:
            subtrair(n1,n2)
        case 3:
            multiplicar(n1,n2)
        case 4:
            dividir(n1,n2)