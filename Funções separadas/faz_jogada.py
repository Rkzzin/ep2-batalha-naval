# Faz a jogada e confere se acertou ou errou
def faz_jogada(tabuleiro, linha, coluna):

    # Caso tenha navio na posição, substitui o 1 por X
    if tabuleiro[linha][coluna] == 1 or tabuleiro[linha][coluna] == 'X':
        tabuleiro[linha][coluna] = 'X'

    # Caso não tenha navio na posição, substitui o 0 por -
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

tabuleiro = [
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]

linha = 1
coluna = 1
resultado = faz_jogada(tabuleiro, linha, coluna)
print(resultado)