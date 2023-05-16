import random

palavra = ["smartphone", "computador", "notebook", "programador", "python", "microsoft", "javascript"]
palavra_recebida = random.choice(palavra)
vetor_aux2 = []
vetor_aux = ["_"]*len(palavra_recebida)
acertou = False
cont = 0
# boneco = "cabeça, corpo, braço esq, braço direito, perna esq, perna direita, nesse caso sao 6 condições


print("Bem vindo ao jogo da forca! O tema do jogo é tecnologia!")
print("="*56)

for x in palavra_recebida:
    vetor_aux2.append(x)



while '_' in vetor_aux:
    acertou = False
    print(vetor_aux)
    pergunta = input("Informe uma letra: ")
    if pergunta in palavra_recebida:
        for n in range(len(palavra_recebida)):
            if pergunta == vetor_aux2[n]:
                del vetor_aux[n]
                vetor_aux.insert(n,pergunta)
                acertou = True
    if acertou:
        print("letra correta!")
    else:
        cont += 1
        match cont:
            case 1:
                print("cabeça adicionada ao boneco!")
            case 2:
                print("cabeça, corpo adicionada ao boneco!")
            case 3:
                print("cabeça, corpo, braço esquerdo adicionada ao boneco!")
            case 4:
                print("cabeça, corpo, braço esq e direito adicionada ao boneco!")
            case 5:
                print("cabeça, corpo, braço esq+dir e perna esq adicionada ao boneco!")
            case 6:
                print("boneco completado, você perdeu!")
                break
print("="*40)
if '_' not in vetor_aux:
    print(f"Você ganhou! A palavra é: {palavra_recebida}")
else:
    print(f"Você perdeu! A palavra era: {palavra_recebida}")

