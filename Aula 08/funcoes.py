def somar(*numeros):
    total = 0
    for x in numeros:
        total+=x
    return total
def subtrair(n1,n2):
    return n1-n2
def multiplicar(n1,n2):
    return n1*n2
def dividir(n1,n2):
    return n1/n2
def repetir_piramide(num):
    for x in range(1,num+1):
        print(str(x)*x)
def piramide_soma(num):
    for x in range(1,num+1):
        for y in range(1,x+1):
            print(y, end= " ")
def vogais(t):
    cont = 0
    for x in t:
        if x in "aeiouAEIOU":
            cont+=1
    print(f"O texto contém {cont} vogais")
def valor_total(nome,qtd,preco):
    valor = preco*qtd
    return nome,valor
def imprimir_inverter_texto (texto):
    cont = 0
    texto_invertido = ""
    for x in range (len(texto)-1,-1,-1):
        texto_invertido += texto[x]
        if texto[x] != " ":
            cont += 1
    print(cont)
    print(texto_invertido)
def criar_nova_lista(a):
    nova_lista = []
    for x in a:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)