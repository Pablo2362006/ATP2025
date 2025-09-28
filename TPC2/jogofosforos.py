# Jogo da caixa de fósforos
import random
# Jogo da caixa de fósforos
import random

def jogo_fosforos():
    fosforos = 21
    print("Bem-vindo ao jogo da caixa de fósforos!")
    print("Quem retirar o último fósforo perde.")
    while True:
        escolha = input("Quem começa? (u para utilizador, c para computador): ").lower()
        if escolha in ('u', 'c'):
            break
        else:
            print("Resposta inválida. Por favor, escreva 'u' ou 'c'.")
    primeiro = (escolha == 'c')
    vez_do_computador = primeiro
    jogada_computador.ultima_jogada_utilizador = 0
    jogada_computador.primeira_jogada = True if vez_do_computador else False
    jogada_computador.ultima_jogada_computador = 0

    while fosforos > 0:
        if vez_do_computador:
            if primeiro:
                n = jogada_computador(fosforos, True)
            else:
                n = jogada_computador(fosforos, False)
            print(f"Computador retira {n} fósforo(s).")
            fosforos -= n
            if fosforos == 0:
                print("O computador retirou o último fósforo. Utilizador vence!")
                break
            vez_do_computador = False
        else:
            n = jogada_utilizador(fosforos)
            jogada_computador.ultima_jogada_utilizador = n
            fosforos -= n
            if fosforos == 0:
                print("O utilizador retirou o último fósforo. Computador vence!")
                break
            vez_do_computador = True

def jogada_utilizador(fosforos):
    while True:
        try:
            n = int(input(f"Fósforos restantes: {fosforos}. Quantos quer retirar (1-4)? "))
            if 1 <= n <= 4 and n <= fosforos:
                return n
            else:
                print("Jogada inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número inteiro.")

def jogada_computador(fosforos, primeiro):
    # Estratégia ótima: nunca retirar o último fósforo se puder evitar
    if fosforos <= 4:
        # Se restam 2, 3 ou 4 fósforos, retirar o suficiente para deixar 1
        if fosforos > 1:
            return fosforos - 1
        else:
            return 1  # Se só resta 1, é obrigado a perder
    if primeiro:
        # Primeira jogada do computador: escolher aleatoriamente entre 1 e 4
        if jogada_computador.primeira_jogada:
            n = random.randint(1, 4)
            jogada_computador.primeira_jogada = False
            jogada_computador.ultima_jogada_computador = n
            return n
        else:
            # Depois, garantir múltiplos de 5
            n = 5 - jogada_computador.ultima_jogada_utilizador
            if n < 1 or n > 4 or n > fosforos:
                n = min(fosforos, random.randint(1, min(4, fosforos)))
            jogada_computador.ultima_jogada_computador = n
            return n
    else:
        n = 5 - jogada_computador.ultima_jogada_utilizador
        if n < 1 or n > 4 or n > fosforos:
            n = min(fosforos, random.randint(1, min(4, fosforos)))
        return n

if __name__ == "__main__":
    jogo_fosforos()
