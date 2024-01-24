# Importe as bibliotecas necessárias
import random

# Defina as constantes do jogo
JOGADAS = ["pedra", "papel", "tesoura"]

# Inicialize o jogo
def iniciar_jogo():
    # Bem-vindo o jogador
    print("\nBem-vindo ao jogo de pedra, papel e tesoura de Bruno Gondran!")

    # Mostre as regras do jogo
    print("As regras são simples:")
    print("* Pedra bate em tesoura")
    print("* Tesoura corta papel")
    print("* Papel embrulha pedra")

    # Inicialize o placar
    jogador_vitorias = 0
    computador_vitorias = 0

    # Comece o loop do jogo
    while True:
        # Solicite a jogada do jogador
        jogador = input("\nQual é a sua jogada? (pedra, papel ou tesoura): ").lower()

        # Verifique se a escolha do jogador é válida
        if jogador not in JOGADAS:
            print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
            continue

        # Escolha a jogada do computador
        computador = random.choice(JOGADAS)

        # Determine o vencedor
        vencedor = determinar_vencedor(jogador, computador)

        # Exiba o resultado do jogo
        jogador_vitorias, computador_vitorias = exibir_resultado(jogador, computador, vencedor, jogador_vitorias, computador_vitorias)

        # Pergunte se o jogador quer jogar novamente
        resposta = input("\nDeseja jogar novamente? (S/N): ")
        if resposta.lower() == "n":
            break

    # Exiba o placar
    print("\nPlacar:")
    print("Jogador:", jogador_vitorias)
    print("Computador:", computador_vitorias)

# Determine o vencedor da partida
def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate"

    if jogador == "pedra":
        return "Jogador" if computador == "tesoura" else "Computador"

    if jogador == "papel":
        return "Jogador" if computador == "pedra" else "Computador"

    if jogador == "tesoura":
        return "Jogador" if computador == "papel" else "Computador"

# Exiba o resultado da partida
def exibir_resultado(jogador, computador, vencedor, jogador_vitorias, computador_vitorias):
    print(f"\nVocê escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    if vencedor == "Empate":
        print("Empate!")
    elif vencedor == "Jogador":
        print("Parabéns, você venceu!")
        jogador_vitorias += 1
    else:
        print("O computador venceu!")
        computador_vitorias += 1

    return jogador_vitorias, computador_vitorias

# Inicialize o jogo
iniciar_jogo()
