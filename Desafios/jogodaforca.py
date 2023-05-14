import random

palavra = ["smartphone","computador","impressora"]
palavra_recebida = random.choice(palavra)
vetor_aux2 = []
vetor_aux = ["_"]*len(palavra_recebida)
# boneco = "cabeça, corpo, braço esq, braço direito, perna esq, perna direita, nesse caso sao 6 condições


print("Bem vindo ao jogo da forca! O tema do jogo é tecnologia!")
cont = 0
for x in palavra_recebida:
    vetor_aux2.append(x)
index = 0
#impressora
print(palavra_recebida)
index = 0
acertou = 0
while '_' in vetor_aux:
    acertou = False
    print(vetor_aux)
    pergunta = input("Informe uma letra: ")
    for index, letra in enumerate(palavra_recebida):
        if pergunta == letra and vetor_aux[index] == '_':
            vetor_aux[index] = pergunta
            print(vetor_aux[index],index)
            acertou = True
    if acertou:
        print("Você acertou!")
    else:
        cont+=1
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













# while vetor_aux != vetor_aux2:
#     acertou = False
#     for y in vetor_aux:
#         print(vetor_aux)
#         pergunta = input("Informe uma letra: ")
#         if pergunta in palavra_recebida:
#             for n in range(len(palavra_recebida)):
#                 if pergunta == vetor_aux2[n]:
#                     del vetor_aux[n]
#                     vetor_aux.insert(n,pergunta)
#                     acertou = True
#         if acertou:
#             print("letra correta!")
#         else:
#             cont += 1
#         match cont:
#             case 1:
#                 print("cabeça adicionada ao boneco!")
#             case 2:
#                 print("cabeça, corpo adicionada ao boneco!")
#             case 3:
#                 print("cabeça, corpo, braço esquerdo adicionada ao boneco!")
#             case 4:
#                 print("cabeça, corpo, braço esq e direito adicionada ao boneco!")
#             case 5:
#                 print("cabeça, corpo, braço esq+dir e perna esq adicionada ao boneco!")
#             case 6:
#                 print("boneco completado, você perdeu!")
#                 break