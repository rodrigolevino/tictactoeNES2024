from modulo_jogovelha import jogovelha

jogador1 = jogovelha.JogadorHumano("X", "Rodrigo")
jogador2 = jogovelha.JogadorComputador("O", "ALEATORIA", "Bot1")
jogador3 = jogovelha.JogadorComputador("X", "ALEATORIA", "Bot2")
jogo = jogovelha.JogoVelha(jogador1, jogador2)
jogo.jogar()

# Ao escolher a casa considere linhas e colunas de 1 a 3.
# Ex: Casa '1 1' é a primeira do tabuleiro