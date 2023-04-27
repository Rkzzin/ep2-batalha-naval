##################################
###### DEFINIÇÃO DAS FUNÇÕES #####
##################################

from arquivo_geral_das_funções import *
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
        [[7, 6]]
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

    # Printa os tabuleiros:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    ###################################
    ######## VEZ DO JOGADOR ###########
    ###################################

    # Linha a ser atacada:
    linha = int(input('Linha: '))
    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Linha: '))
    
    # Coluna a ser atacada:
    coluna = int(input('Coluna: '))
    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Coluna: '))

    # Verifica se a posição já foi informada anteriormente:
    while [linha, coluna] in jogadas_jogador:

        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')

        linha = int(input('Linha: '))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Coluna: '))

    jogadas_jogador.append([linha, coluna])
    

    # Faz a jogada e verifica se afundou algum navio:
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    
    else:

        ###################################
        ######## VEZ DO OPONENTE ##########
        ###################################

        # Jogada do oponente:
        linha = rd.randint(0, 9)
        coluna = rd.randint(0, 9)

        while [linha, coluna] in jogadas_oponente:
            linha = rd.randint(0, 9)
            coluna = rd.randint(0, 9)

        jogadas_oponente.append([linha, coluna])

        print(f'Seu oponente está atacando na linha {linha} e coluna {coluna}')

        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha, coluna)

        if afundados(frota_jogador, tabuleiro_jogador) == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False