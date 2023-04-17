n = 1
media = 0
while n <= 10:
    num = float(input(f"Digite o valor {n} da média aritmética: \n"))
    n = n + 1
    media = num + media
print("A média aritmética dos 10 valores foram: ", media/10)
