n = int(input("digite um número N para o intervalo entre 1 e N: \n"))
if n > 0:
    for x in range(1,n+1):
            print(x)
elif n <= 0:
    print("O valor N não pode ser menor ou igual a 0!!")