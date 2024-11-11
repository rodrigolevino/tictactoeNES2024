import numpy as np

class Tabuleiro:
    def __init__(self) -> None:
        ''' Inicia as casas vazias em formato de lista
        '''
        self.casas = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def pegar_tabuleiro(self) -> list[list[str]]:
        ''' Utiliza um for que passa por 'self.casas' e faz uma matriz

        Returns:
            list[list[str]]: Retorna uma matriz representando as casas
        '''
        matriz_casas = []
        for i in range(0, 3):
            matriz_casas.append([])
            for j in range(0, 3):
                matriz_casas[i].append(self.casas[3*i + j])
        return matriz_casas

    def marcar_casa(self, pos: tuple[int, int], valor: str) -> None:
        ''' Marca a casa com o valor do usuário

        Args:
            pos (tuple[int, int]): Uma tupla representando a posição da casa
            valor (str): É o símbolo do usuário que fez a jogada
        '''
        # Calcula o index de uma lista de 0 a 8 dado a linha e coluna
        index_casa = pos[0] * 3 + pos[1]
        if self.casas[index_casa] == " ":
            self.casas[index_casa] = valor
        else:
            print("A casa já foi marcada!")

    def imprimir_tabuleiro(self) -> None:
        ''' Utiliza um for que passa pela matriz das casas e imprime
        '''
        matriz_casas = self.pegar_tabuleiro()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f"|{matriz_casas[i][j]}", end="")
            print("|")


class Jogador:
    def __init__(self, simbolo: str, nome: str) -> None:
        ''' Armazena os valores

        Args:
            simbolo (str): Símbolo que representará o jogador
            nome (str): Nome do jogador para identifica-lo
        '''
        self.simbolo = simbolo
        self.nome = nome

    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int, int]:
        pass


class JogadorHumano(Jogador):
    def __init__(self, simbolo: str, nome: str) -> None:
        super().__init__(simbolo, nome)

    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int, int]:
        ''' Faz a jogada do usuário no tabuleiro

        Args:
            tabuleiro (Tabuleiro): É o tabuleiro usado no jogo

        Returns:
            Recebe uma tupla que representa a jogada do usuário
        '''
        print(f"Jogador {self.nome}")
        jogada = input("Digite sua jogada no formato 'lin col': ")
        # Separa o texto dividido pelo usuário entre espaço
        # E o transforma em uma tupla de inteiros
        jogada = jogada.split()
        tupla_jogada = (int(jogada[0])-1, int(jogada[1])-1)
        tabuleiro.marcar_casa(tupla_jogada, self.simbolo)


class JogadorComputador(Jogador):
    def __init__(self, simb: str, estrategia: str, nome: str) -> None:
        '''
        Args:
            simb (str): Símbolo utilizado pelo jogador
            estrategia (str): Estrategia que o computador vai utilizar
        '''
        self.nome = nome
        self.estrategia = estrategia
        super().__init__(simb, nome)

    def fazer_jogada(self, tab: Tabuleiro) -> tuple[int, int]:
        ''' Faz a jogada baseada na estratégia

        Args:
            tab (Tabuleiro): É o tabuleiro utilizado no jogo

        Returns:
            Escolhe uma casa vazia e retorna ela em forma de tupla de inteiros
        '''
        print(f"Jogador {self.nome}")
        if self.estrategia.lower() == "aleatoria":
            casas_vazias = []
            matriz_casas = tab.pegar_tabuleiro()
            # Preenche a lista de casas vazias com tuplas
            for i in range(0, 3):
                for j in range(0, 3):
                    if matriz_casas[i][j] == " ":
                        casas_vazias.append((i, j))
            # Escolhe um index da lista de casas vazias e
            # Retorna a tupla no index escolhido
            idx_escolhido = np.random.choice(len(casas_vazias))
            tab.marcar_casa(casas_vazias[idx_escolhido], self.simbolo)


class JogoVelha:
    def __init__(self, jogador1: Jogador, jogador2: Jogador) -> None:
        ''' Armazena os valores necessários para o jogo

        Args:
            jogador1 (Jogador): Representa o jogador 1 do jogo
            jogador2 (Jogador): Representa o jogador 2 do jogo

        '''
        self.jogadores = [jogador1, jogador2]
        np.random.shuffle(self.jogadores)
        self.turno = 0
        self.tabuleiro = Tabuleiro()

    def jogador_atual(self) -> Jogador:
        '''
        Returns:
            Retorna o jogador do turno atual
        '''
        return self.jogadores[self.turno%2]

    def checar_fim_de_jogo(self) -> str | None:
        ''' Checa se o jogo acabou na horiz, vert, diag, deu empate, ou não

        Returns:
            Pode retornar uma string representando o resultado, ou None
        '''
        matriz_tab = self.tabuleiro.pegar_tabuleiro()
        simb_jogador1 = self.jogadores[0].simbolo

        # Faz a matriz transposta para verificar as verticais
        matriz_t = np.array(matriz_tab)
        matriz_t = matriz_t.T
        matriz_t = matriz_t.tolist()

        for i in range(0, 3):
            # Verifica se o jogador ganhou na horizontal
            if matriz_tab[i].count(matriz_tab[i][0]) == 3:
                if matriz_tab[i][0] == " ":
                    continue
                if matriz_tab[i][0] == simb_jogador1:
                    return f"{self.jogadores[0].nome} ganhou!"
                else:
                    return f"{self.jogadores[1].nome} ganhou!"

            # Verifica se o jogador ganhou na vertical utilizando transposta
            if matriz_t[i].count(matriz_t[i][0]) == 3:
                if matriz_t[i][0] == " ":
                    continue
                if matriz_t[i][0] == simb_jogador1:
                    return f"{self.jogadores[0].nome} ganhou!"
                else:
                    return f"{self.jogadores[1].nome} ganhou!"

        # Armazena as diagonais em uma lista de lista
        diagonais =[[], []]
        for i in range(0, 3):
            diagonais[0].append(matriz_tab[i][i])
            diagonais[1].append(matriz_tab[i][2-i])

        # Verifica se o jogador ganhou na vertical
        for i in range(0, 2):
            if diagonais[i].count(diagonais[i][0]) == 3:
                if diagonais[i][0] == " ":
                    continue
                if diagonais[i][0] == simb_jogador1:
                    return f"{self.jogadores[0].nome} ganhou!"
                else:
                    return f"{self.jogadores[1].nome} ganhou!"

        # Vê se ainda tem casas disponíveis no tabuleiro
        if " " in  self.tabuleiro.casas:
            return None

        # Caso nenhum dos casos tenha ocorrido, deu empate
        return "Empate!"

    def jogar(self) -> None:
        ''' Repete o jogo até acabar utilizando um while
        '''
        while True:
            jogador_atual = self.jogador_atual()
            # Aumenta em 1 o turno para alterar o jogador da próxima rodada
            self.turno += 1
            jogador_atual.fazer_jogada(self.tabuleiro)
            self.tabuleiro.imprimir_tabuleiro()
            resultado = self.checar_fim_de_jogo()
            # Se nenhum caso de resultado ocorreu, o jogo continua
            if resultado == None:
                continue
            else:
                print(resultado)
                break
