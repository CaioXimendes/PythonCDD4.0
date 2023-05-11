def vogais(t):
    cont = 0
    for x in t:
        if x in "aeiouAEIOU":
            cont+=1
    print(f"O texto contém {cont} vogais")

texto = "O rato roeu a roupa do rei de roma"
vogais(texto)