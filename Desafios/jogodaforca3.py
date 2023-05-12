import random

lista = ["smartphone", "computador", "notebook", "programador", "python", "microsoft", "javascript"]
palavra_recebe = random.choice(lista)
lista_2 = ['_'] * len(palavra_recebe)
cont = 0

print("Bem vindo ao jogo da forca, o tema é tecnologia! \n")

while '_' in lista_2:
    acertou = False

    print(lista_2)
    pergunta = input("Informe uma letra: ")

    for i, letra in enumerate(palavra_recebe):
        if letra == pergunta and lista_2[i] == '_':
            lista_2[i] = pergunta
            acertou = True
    if acertou:
        print("você acertou!")
    else:
        cont += 1
        match cont:
            case 1:
                print("cabeça adicionada!")
            case 2:
                print("tronco adicionado!")
            case 3:
                print("braço direito adicionado!")
            case 4:
                print("braço esquerdo adicionado!")
            case 5:
                print("perna direita adicionada!")
            case 6:
                print("boneco completado!")
                break

if '_' not in lista_2:
    print(f"parabéns! você acertou a palavra: {palavra_recebe}")
else:
    print("Você perdeu, tente a próxima!")
