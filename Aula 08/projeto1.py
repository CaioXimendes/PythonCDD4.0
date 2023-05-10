

"""for x in range (num):
    for y in range (x):
        print(x, end = " ")
    print()"""
def repetir_piramide(num):
    for x in range(1,num+1):
        print(str(x)*x)

numero = int(input("Informe um número: "))
repetir_piramide(numero)