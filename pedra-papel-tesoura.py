# Importando as bibliotecas necessárias
import random

# Definindo as constantes do jogo
JOGADAS = ["pedra", "papel", "tesoura"]

# Inicializando o jogo
def iniciar_jogo():
    # Bem-vindo ao jogador(a)
    print("\nBem-vindo ao jogo de pedra, papel e tesoura de Bruno Gondran!")

    # Mostrando as regras do jogo
    print("As regras são simples:")
    print("* Pedra bate em tesoura")
    print("* Tesoura corta papel")
    print("* Papel embrulha pedra")

    # Inicializando o placar
    jogador_vitorias = 0
    computador_vitorias = 0

    # Começando o loop do jogo
    while True:
        # Solicitando a jogada do jogador
        jogador = input("\nQual é a sua jogada? (pedra, papel ou tesoura): ").lower()

        # Verificando se a escolha do jogador é válida
        if jogador not in JOGADAS:
            print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
            continue

        # Escolhendo a jogada do computador
        computador = random.choice(JOGADAS)

        # Determinando o vencedor
        vencedor = determinar_vencedor(jogador, computador)

        # Exibindo o resultado do jogo
        jogador_vitorias, computador_vitorias = exibir_resultado(jogador, computador, vencedor, jogador_vitorias, computador_vitorias)

        # Perguntando se o jogador quer jogar novamente
        resposta = input("\nDeseja jogar novamente? (S/N): ")
        if resposta.lower() == "n":
            break

    # Exibindo o placar
    print("\nPlacar:")
    print("Jogador:", jogador_vitorias)
    print("Computador:", computador_vitorias)

# Determinando o vencedor da partida
def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate"

    if jogador == "pedra":
        return "Jogador" if computador == "tesoura" else "Computador"

    if jogador == "papel":
        return "Jogador" if computador == "pedra" else "Computador"

    if jogador == "tesoura":
        return "Jogador" if computador == "papel" else "Computador"

# Exibindo o resultado da partida
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

# Inicializando o jogo
iniciar_jogo()
