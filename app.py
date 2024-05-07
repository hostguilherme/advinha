def jogo_adivinhacao():

    print("Jogador 1: Por favor, escolha um número entre 1 e 100 para ser adivinhado.")
    numero_secreto = int(input("Digite o número secreto: "))


    while numero_secreto < 1 or numero_secreto > 100:
        print("Por favor, escolha um número entre 1 e 100.")
        numero_secreto = int(input("Digite o número secreto: "))


    tentativas = 0
    adivinhado = False

    print("Jogador 2: Tente adivinhar o número que o Jogador 1 escolheu.")


    while not adivinhado:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                adivinhado = True
                print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")

        except ValueError:
            print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    jogo_adivinhacao()
