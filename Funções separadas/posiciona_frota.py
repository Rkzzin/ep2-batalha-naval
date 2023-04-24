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


frota = {'porta-aviões': [[[1, 5], [1, 6], [1, 7], [1, 8]]],
         'navio-tanque': [[[6, 1], [6, 2], [6, 3]],
                          [[4, 7], [5, 7], [6, 7]]],
         'contratorpedeiro': [[[1, 1], [2, 1]],
                              [[2, 3], [3, 3]],
                              [[9, 1], [9, 2]]],
         'submarino': [[[0, 3]],
                       [[4, 5]],
                       [[8, 9]],
                       [[8, 4]]]}

resultado = posiciona_frota(frota)
print(resultado)
