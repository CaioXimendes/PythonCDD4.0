from funcoes import valor_total

estoque = valor_total("banana", 5, 10)
print(f"O nome do produto é: {estoque[0]} e seu valor é: {estoque[1]}")
nome, valor = estoque = valor_total("banana", 5, 10)
print(f"O produto: {nome} custou: {valor}")

# () são tuplas, colocando virgula no return, ele retornará uma tupla, as tuplas funcionam como as listas, porém são
#como constantes, não se alteram durante a execução do código


