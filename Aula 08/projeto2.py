def piramide_soma(num):
    for x in range(1,num+1):
        for y in range(1,x+1):
            print(y, end= " ")
        print()
numero = int(input("Informe um número: "))
piramide_soma(numero)