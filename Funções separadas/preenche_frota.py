def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    # Verifica se o navio já está na frota
    if nome_navio not in frota:
        # Caso não esteja, adiciona o navio à frota
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]

    # Senão, adiciona as posições do tipo de navio à frota    
    else:
        frota[nome_navio] += [define_posicoes(linha, coluna, orientacao, tamanho)]

    return frota
