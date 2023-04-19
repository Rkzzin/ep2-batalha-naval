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


## Loop do jogo ##
