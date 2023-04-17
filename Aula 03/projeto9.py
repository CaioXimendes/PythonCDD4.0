intervalo = int(input("Digite o limite do intervalo dos números: \n"))
for x in range(1,intervalo):
    if x % 2 != 0:
        print(x)