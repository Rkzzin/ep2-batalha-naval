# Função que define as posições do navio
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

# Função que verifica se a posição é válida para o novo navio
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    # Verifica se as posições estão fora do tabuleiro
    for nova_posicao in novas_posicoes:
        if nova_posicao[0] < 0 or nova_posicao[0] > 9 or nova_posicao[1] < 0 or nova_posicao[1] > 9:
            return False

    # Verifica se as posições já estão ocupadas
    for posicoes_ocupadas in frota.values():
        for posicoes in posicoes_ocupadas:
            for posicao in posicoes:
                if posicao in novas_posicoes:
                    return False

    return True


frota = {
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
}
linha = 1
coluna = 5
orientacao = 'horizontal'
tamanho = 4
resultado = posicao_valida(frota, linha, coluna, orientacao, tamanho)
print(resultado)