num_1 = float(input("Informe o número 01: "))
num_2 = float(input("Informe o número 02: "))
num_3 = float(input("Informe o número 03: "))
a = 0

if num_1 > num_2 and num_1 > num_3:
    a = num_1
    print(f"maior número é: {a}")
elif num_2 > num_1 and num_2 > num_3:
    a = num_2
    print(f"maior número é: {a}")
else:
    a = num_3
    print(f"maior número é: {a}")