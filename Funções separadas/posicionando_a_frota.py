# Funções posteriores:
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

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    # Verifica se o navio já está na frota
    if nome_navio not in frota:
        # Caso não esteja, adiciona o navio à frota
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]

    # Senão, adiciona as posições do tipo de navio à frota    
    else:
        frota[nome_navio] += [define_posicoes(linha, coluna, orientacao, tamanho)]

    return frota


# Parâmetros:
disponíveis = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
lista_tamanhos = [4, 3, 2, 1]
orientações_disp = {1: 'vertical', 2: 'horizontal'}

# Frota do jogador:
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

# Quantidade máxima de cada embarcação:
#   Porta aviões = 1
#   Navio tanque = 2
#   Contratorpedeiro = 3
#   Submarino = 4


# Loop principal que preeche a frota:
quantidade_embarcacoes = 0

while quantidade_embarcacoes < 10:
    # Verifica qual tipo de embarcação deve ser inserida:
    if quantidade_embarcacoes == 0:
        print(f'Insira as informações referentes ao navio {disponíveis[0]} que possui tamanho {lista_tamanhos[0]}')
        tamanho = lista_tamanhos[0]
        nome_navio = disponíveis[0]
    
    elif quantidade_embarcacoes <= 2:
        print(f'Insira as informações referentes ao navio {disponíveis[1]} que possui tamanho {lista_tamanhos[1]}')
        tamanho = lista_tamanhos[1]
        nome_navio = disponíveis[1]
    
    elif quantidade_embarcacoes <= 5:
        print(f'Insira as informações referentes ao navio {disponíveis[2]} que possui tamanho {lista_tamanhos[2]}')
        tamanho = lista_tamanhos[2]
        nome_navio = disponíveis[2]

    else:
        print(f'Insira as informações referentes ao navio {disponíveis[3]} que possui tamanho {lista_tamanhos[3]}')
        tamanho = lista_tamanhos[3]
        nome_navio = disponíveis[3]
        orientação = orientações_disp[1]

    # Recebe as informações do usuário:
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if quantidade_embarcacoes <= 5:
        orientação = int(input('Orientação ([1] Vertical | [2] Horizontal): '))
        orientação = orientações_disp[orientação]

    # Verifica se a posição é válida:
    if posicao_valida(frota, linha, coluna, orientação, tamanho):
        frota = preenche_frota(frota, nome_navio, linha, coluna, orientação, tamanho)
        quantidade_embarcacoes += 1
    else:
        print('Esta posição não está válida!')

print(frota)