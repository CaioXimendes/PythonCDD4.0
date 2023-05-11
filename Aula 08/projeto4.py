def valortotal(nome,qtd,valor):
    return qtd*valor,nome

estoque = valortotal("banana",5,1)
print(estoque)

# () são tuplas, colocando virgula no return, ele retornará uma tupla, as tuplas funcionam como as listas, porém são
#como constantes, não se alteram durante a execução do código