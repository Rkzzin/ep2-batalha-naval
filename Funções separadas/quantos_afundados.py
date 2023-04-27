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


frota = {
    "porta-aviões": [
        [[1, 5], [1, 6], [1, 7], [1, 8]]
    ],
    "navio-tanque": [
        [[6, 1], [6, 2], [6, 3]],
        [[4, 7], [5, 7], [6, 7]]
    ],
    "contratorpedeiro": [
        [[1, 1], [2, 1]],
        [[2, 3], [3, 3]],
        [[9, 1], [9, 2]]
    ],
    "submarino": [
        [[0, 3]],
        [[4, 5]],
        [[8, 9]],
        [[8, 4]]
    ],
}
tabuleiro = [
    [0, '-', '-', 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 'X', 'X', 'X', 'X', 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, '-', '-', '-', '-', 0, 0],
    [0, '-', 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, '-', 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 'X', 0, 0, 0, 0, 1],
    [0, 1, 1, '-', '-', '-', '-', '-', '-', '-']
]
resultado = afundados(frota, tabuleiro)
print(resultado)
