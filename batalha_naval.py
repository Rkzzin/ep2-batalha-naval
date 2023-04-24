## Funções ##

# Define as posições do navio de acordo com a orientação
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    # Define as posições caso a orientação seja horizontal
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    
    # Define as posições caso a orientação seja vertical
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])

    return posicoes


# Preenche a frota com os navios
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    # Verifica se o navio já está na frota
    if nome_navio not in frota:
        # Caso não esteja, adiciona o navio à frota
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]

    # Senão, adiciona as posições do tipo de navio à frota    
    else:
        frota[nome_navio] += [define_posicoes(linha, coluna, orientacao, tamanho)]

    return frota

# Faz a jogada e confere se acertou ou errou
def faz_jogada(tabuleiro, linha, coluna):

    # Caso tenha navio na posição, substitui o 1 por X
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'

    # Caso não tenha navio na posição, substitui o 0 por -
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro


# Retorna o tabuleiro com as posições dos navios
def posiciona_frota(frota):
    # Cria o tabuleiro
    tabuleiro = [[0]*10 for _ in range(10)]

    # Preenche o tabuleiro com as posições da frota
    for posicoes in frota.values():
        
        # Percorre as posições do navio e marca-as no tabuleiro
        for posicao in posicoes:
            tamanho = len(posicao)
            for i in range(tamanho):
                tabuleiro[posicao[i][0]][posicao[i][1]] = 1

    return tabuleiro


# Conta o número de navios afundados
def afundados(frota, tabuleiro):
    afundados = 0

    # Percorre a frotas e conta os navios afundados
    for navio in frota:
        
        # Percorre as posições do navio e verifica se todas foram atingidas
        for posicoes in frota[navio]:
            i = 0
            for posicao in posicoes:
                if tabuleiro[posicao[0]][posicao[1]] == 'X':
                    i += 1
            if i == len(posicoes):
                afundados += 1
    
    return afundados

