def computador_adivinha_numero():
    print("Pense num número entre 1 e 100 e não diga ao computador!")
    input("Quando estiver pronto, pressione Enter...")
    baixo = 1
    alto = 100
    tentativas = 0
    max_tentativas = 10

    while tentativas < max_tentativas:
        palpite = (baixo + alto) // 2
        tentativas += 1
        print(f"Tentativa {tentativas}: O computador acha que é {palpite}.")
        resposta = input("Está correto (c), muito baixo (b) ou muito alto (a)? ").lower()
        if resposta == 'c':
            print(f"O computador adivinhou o seu número em {tentativas} tentativas!")
            break
        elif resposta == 'b':
            baixo = palpite + 1
        elif resposta == 'a':
            alto = palpite - 1
        else:
            print("Resposta inválida. Use 'c', 'b' ou 'a'.")
            tentativas -= 1
        if baixo > alto:
            print("Parece que houve um erro nas respostas. Tente novamente!")
            break
    if tentativas == max_tentativas:
        print("O computador não conseguiu adivinhar o seu número!")
import random

def jogar_adivinha_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    print("Bem-vindo ao jogo de Adivinha o Número!")
    print("Tente adivinhar o número entre 1 e 100.")
    print(f"Você tem {max_tentativas} tentativas.")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("Por favor, escolha um número entre 1 e 100.")
                continue

            if palpite < numero_secreto:
                print("Muito baixo!")
            elif palpite > numero_secreto:
                print("Muito alto!")
            else:
                print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")


    if tentativas == max_tentativas and palpite != numero_secreto:
        print(f"Suas tentativas acabaram! O número era {numero_secreto}.")


if __name__ == "__main__":
    print("Escolha o modo de jogo:")
    print("1 - Você tenta adivinhar o número do computador")
    print("2 - O computador tenta adivinhar o seu número")
    modo = input("Digite 1 ou 2: ")
    if modo == '1':
        jogar_adivinha_numero()
    elif modo == '2':
        computador_adivinha_numero()
    else:
        print("Opção inválida.")