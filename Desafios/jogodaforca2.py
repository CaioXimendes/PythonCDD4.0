import random

palavra = ["smartphone", "computador", "impressora"]
palavra_recebida = random.choice(palavra)
vetor_aux = ['_'] * len(palavra_recebida)

print("Bem-vindo ao jogo da forca! O tema do jogo é tecnologia!")
cont = 0

while '_' in vetor_aux:
    print(vetor_aux)
    pergunta = input("Informe uma letra: ")

    acertou = False
    for i, letra in enumerate(palavra_recebida):
        if letra == pergunta and vetor_aux[i] == '_':
            vetor_aux[i] = pergunta
            acertou = True

    if acertou:
        print("Letra correta!")
    else:
        cont += 1
        match cont:
            case 1:
                print("Cabeça adicionada ao boneco!")
            case 2:
                print("Cabeça e corpo adicionados ao boneco!")
            case 3:
                print("Cabeça, corpo e braço esquerdo adicionados ao boneco!")
            case 4:
                print("Cabeça, corpo, braço esquerdo e braço direito adicionados ao boneco!")
            case 5:
                print("Cabeça, corpo, braço esquerdo, braço direito e perna esquerda adicionados ao boneco!")
            case 6:
                print("Boneco completado!")
                break

# Verifica se o jogador ganhou
if '_' not in vetor_aux:
    print(f"Parabéns! Você acertou a palavra: {palavra_recebida}")
else:
    print(f"Você perdeu! A palavra era: {palavra_recebida}")