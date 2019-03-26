import os


print("*********************************")
print(" Bem-vindo ao jogo Adivinha Quem")
print("*********************************")
print("\n-----------Desafiante-----------\n")
personagem = input("\nDigite o nome de um personagem para ser descoberto: ")

dica = []

for n in range (1, 6):
    print("\nDigite a dica", n , ": ")
    dica.append(input())      #Salvar as dicas no vetor

os.system('cls')  #Limpar a tela

print("----------Adivinhador-----------\n")
pontos = 5
for n_chutes in range(5):
    chute = int(input("\nEscolha uma dica de 1 a 5: "))
    chute -= 1
    #print(dica)
    print('\nDica {}: {}'.format(chute+1,dica[chute]))

    resp = input("\nQuer chutar 'sim' ou 'nao'? ")
    if (resp.upper() == "NAO"):
        pontos -= 1
        if (n_chutes == 4):
            os.system('cls')  # Limpar a tela
            print("\n*** Infelizmente você perdeu! :c  0 pontos ***")
    elif (resp.upper() == "SIM"):
        final = input("Qual o personagem? ")
        if (final.upper() == personagem.upper()):
            print("PARABÉNS! VOCê ACERTOU E GANHOU {} PONTOS".format(pontos))
            break
        else:
            print("Erroooou! Passou longe... Tente na próxima")
            break
    else:
        print("Digite uma resposta válida!")

#for n in dica:
#    print("Dica {}: {}".format(dica.index(n)+1,n))  #Exibir as dicas

input()  #Pro cmd não fechar