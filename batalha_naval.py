##################################
###### DEFINIÇÃO DAS FUNÇÕES #####
##################################

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
    if tabuleiro[linha][coluna] == 1 or tabuleiro[linha][coluna] == 'X':
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

# Função que printa o tabuleiro
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

import random as rd

##################################
###### DEFINIÇÃO DAS FROTAS ######
##################################

# Frota do oponente:
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[9, 6]]
    ]
}


# Frota do jogador:

# Parâmetros:
disponíveis = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
lista_tamanhos = [4, 3, 2, 1]
orientações_disp = {1: 'vertical', 2: 'horizontal'}

frota_jogador = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

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
    if posicao_valida(frota_jogador, linha, coluna, orientação, tamanho):
        frota_jogador = preenche_frota(frota_jogador, nome_navio, linha, coluna, orientação, tamanho)
        quantidade_embarcacoes += 1
    else:
        print('Esta posição não está válida!')


# Criando os tabuleiros do jogo 
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota_jogador)


########################################
######## LOOP PRINCIPAL DO JOGO ########
########################################

jogando = True
jogadas_jogador = []
jogadas_oponente = []

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    ###################################
    ######## VEZ DO JOGADOR ###########
    ###################################

    # Linha a ser atacada:
    linha = int(input('Em que linha deseja atacar? '))
    while linha < 0 or linha > 9:
        print('linha inválida!')
        linha = int(input('Em que linha deseja atacar? '))
    
    # Coluna a ser atacada:
    coluna = int(input('Em que coluna deseja atacar? '))
    while coluna < 0 or coluna > 9:
        print('coluna inválida!')
        coluna = int(input('Em que coluna deseja atacar? '))


    # Verifica se a posição já foi atacada:
    while [linha, coluna] in jogadas_jogador:

        print(f'A posição linha {linha} e coluna {coluna} já foi atacada anteriormente!')

        linha = int(input('Em que linha deseja atacar? '))
        while linha < 0 or linha > 9:
            print('linha inválida!')
            linha = int(input('Em que linha deseja atacar? '))

        coluna = int(input('Em que coluna deseja atacar? '))
        while coluna < 0 or coluna > 9:
            print('coluna inválida!')
            coluna = int(input('Em que coluna deseja atacar? '))
    
    
    # Adiciona a jogada na lista de jogadas:
    jogadas_jogador.append([linha, coluna])
    

    # Faz a jogada e verifica se afundou algum navio:
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    navios_afundados = 0
    # Verifica se o jogador venceu:
    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:

        ###################################
        ######## VEZ DO OPONENTE ##########
        ###################################

        # Gera uma posição aleatória:
        linha_oponente = rd.randint(0, 9)
        coluna_oponente = rd.randint(0, 9)

        while [linha_oponente, coluna_oponente] in jogadas_oponente:
            linha_oponente = rd.randint(0, 9)
            coluna_oponente = rd.randint(0, 9)
        
        jogadas_oponente.append([linha_oponente, coluna_oponente])

        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}.')

        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

        navios_afundados_jogador = 0

        # Verifica se o oponente venceu:
        if afundados(frota_jogador, tabuleiro_jogador) == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False

            