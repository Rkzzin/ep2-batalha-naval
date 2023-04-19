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

# Loop do jogo
