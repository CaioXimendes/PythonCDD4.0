total_eleitores = int(input("Informe o total de eleitores: "))
votos_brancos = int(input("Informe os votos em branco: "))
votos_nulos = int(input("Informe os votos nulos: "))
votos_validos = int(input("Informe os votos validos: "))
perc_brancos = (votos_brancos/100)*total_eleitores
perc_nulos = (votos_nulos/100)*total_eleitores
perc_validos = (votos_validos/100)*total_eleitores
print(f"O total de votos brancos foi: {perc_brancos}% , votos nulos foi: {perc_nulos}% e válidos foi: {perc_validos}")