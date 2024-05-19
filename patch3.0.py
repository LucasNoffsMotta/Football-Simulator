from Colors import cores
import pygame
from music_mp3 import musica

cor = cores()
pygame.init()




#BLOCO 1  - TIMES

#Dicionario dos times (serao compactados em uma funcao apos os testes):
def times():
    jogadores_flamengo = {
        'Goleiro': [
            {'Nome': 'Diego Alves', 'Posicao' : 'Goleiro','Forca': 84, 'Idade': 36, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Hugo Souza', 'Posicao':'Goleiro','Forca': 75, 'Idade': 23, 'Nacionalidade': 'Brasil'}
        ],
        'Lateral Direito': [
            {'Nome': 'Maurício Isla', 'Posicao':'Lateral Direito','Forca': 81, 'Idade': 33, 'Nacionalidade': 'Chile'},
            {'Nome': 'Rodinei', 'Posicao':'Lateral Direito','Forca': 75, 'Idade': 29, 'Nacionalidade': 'Brasil'}
        ],
        'Zagueiro': [
            {'Nome': 'Gustavo Henrique', 'Posicao':'Zagueiro','Forca': 78, 'Idade': 28, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Bruno Viana', 'Posicao':'Zagueiro','Forca': 77, 'Idade': 26, 'Nacionalidade': 'Portugal'},
            {'Nome': 'Léo Pereira', 'Posicao':'Zagueiro','Forca': 75, 'Idade': 25, 'Nacionalidade': 'Brasil'}
        ],
        'Lateral Esquerdo': [
            {'Nome': 'Filipe Luís', 'Posicao':'Lateral Esquerdo','Forca': 82, 'Idade': 36, 'Nacionalidade': 'Brasil'}
        ],
        'Meio-Campo': [
            {'Nome': 'Willian Arão', 'Posicao':'Meio-Campo','Forca': 80, 'Idade': 29, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Gerson', 'Posicao':'Meio-Campo','Forca': 83, 'Idade': 24, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Everton Ribeiro', 'Posicao':'Meio-Campo','Forca': 82, 'Idade': 32, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Arrascaeta', 'Posicao':'Meio-Campo','Forca': 84, 'Idade': 27, 'Nacionalidade': 'Uruguai'}
        ],
        'Atacante': [
            {'Nome': 'Gabigol', 'Posicao':'Atacante','Forca': 84, 'Idade': 25, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Bruno Henrique', 'Posicao':'Atacante','Forca': 83, 'Idade': 31, 'Nacionalidade': 'Brasil'}
    ]
    }
    jogadores_corinthians = {
        'Goleiro': [
            {'Nome': 'Cássio', 'Posicao':'Goleiro','Forca': 80, 'Idade': 34, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Matheus Donelli', 'Posicao':'Goleiro','Forca': 72, 'Idade': 20, 'Nacionalidade': 'Brasil'}
        ],
        'Lateral Direito': [
            {'Nome': 'Fagner', 'Posicao':'Lateral Direito','Forca': 79, 'Idade': 32, 'Nacionalidade': 'Brasil'},
            {'Nome': 'João Pedro', 'Posicao':'Lateral Direito','Forca': 72, 'Idade': 24, 'Nacionalidade': 'Brasil'}
        ],
        'Zagueiro': [
            {'Nome': 'Gil', 'Posicao':'Zagueiro','Forca': 77, 'Idade': 34, 'Nacionalidade': 'Brasil'},
            {'Nome': 'João Victor', 'Posicao':'Zagueiro','Forca': 74, 'Idade': 24, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Raul Gustavo', 'Posicao':'Zagueiro','Forca': 72, 'Idade': 22, 'Nacionalidade': 'Brasil'}
        ],
        'Lateral Esquerdo': [
            {'Nome': 'Fábio Santos', 'Posicao':'Lateral Esquerdo','Forca': 76, 'Idade': 36, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Lucas Piton', 'Posicao':'Lateral Esquerdo','Forca': 72, 'Idade': 21, 'Nacionalidade': 'Brasil'}
        ],
        'Meio-Campo': [
            {'Nome': 'Gabriel', 'Posicao':'Meio-Campo','Forca': 78, 'Idade': 24, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Roni', 'Posicao':'Meio-Campo','Forca': 73, 'Idade': 22, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Xavier', 'Posicao':'Meio-Campo','Forca': 74, 'Idade': 23, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Vitinho', 'Posicao':'Meio-Campo','Forca': 70, 'Idade': 23, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Matheus Araújo', 'Posicao':'Meio-Campo','Forca': 68, 'Idade': 21, 'Nacionalidade': 'Brasil'}
        ],
        'Atacante': [
            {'Nome': 'Léo Natel', 'Posicao':'Atacante','Forca': 72, 'Idade': 24, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Jô', 'Posicao':'Atacante','Forca': 75, 'Idade': 35, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Felipe', 'Posicao':'Atacante','Forca': 70, 'Idade': 23, 'Nacionalidade': 'Brasil'},
            {'Nome': 'Ruan Oliveira', 'Posicao':'Atacante','Forca': 68, 'Idade': 22, 'Nacionalidade': 'Brasil'}
        ]
    }

    return jogadores_flamengo,jogadores_corinthians

#Funcao para escolher o time:
def escolha_time():

    jogadores_flamengo,jogadores_corinthans = times()

    corinthans = list()
    flamengo = list()
    flamengo.append(jogadores_flamengo)
    corinthans.append(jogadores_corinthans)
    nome_time = str()


    while True:
        escolha_menu = str(input(f'{cor["fundo_preto"]}{cor["verde"]}[1] - Carregar jogo salvo\n[2] - Novo jogo\n: {cor["limpa"]}'))

        if escolha_menu.isnumeric():
            jogo = int(escolha_menu)

            if 0 < jogo < 3:


                #Carregando jogo salvo utilizando uma string:
                if jogo == 1:
                    nome_time = load()

                    if nome_time == 'Corinthans':
                        seu_time = corinthans
                        return seu_time,nome_time

                    elif nome_time == 'Flamengo':
                        seu_time = flamengo
                        return seu_time,nome_time
                    else:
                        print(f'{cor["fundo_preto"]}{cor["vermelho"]}Nenhum arquivo salvo encontrado.{cor["limpa"]}')





                #Iniciando novo jogo:
                elif jogo == 2:

                    time = str(input(f'{cor["fundo_preto"]}{cor["verde"]}Escolha um time:\n{cor["branco"]}[1] - Corinthans\n{cor["vermelho"]}[2] - Flamengo\n: {cor["limpa"]}'))

                    if time.isnumeric():
                        seu_time = int(time)

                        if 0 < seu_time < 3:


                            if seu_time == 1:
                                seu_time = corinthans
                                nome_time = 'Corinthans'
                                return seu_time, nome_time


                            if seu_time == 2:
                                seu_time = flamengo
                                nome_time = 'Flamengo'
                                return seu_time, nome_time
                        else:
                            print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um valor valido.{cor["limpa"]}')
                    else:
                        print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um valor valido.{cor["limpa"]}')
            else:
                print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um valor valido.{cor["limpa"]}')


        else:
            print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um valor valido.')












#BLOCO 2 - UTILIDADES

#Armazena e define esquemas taticos:
def esquemas_taticos(esquema_escolhido):

    seu_time_titular = dict()


    if esquema_escolhido == 1:
        seu_time_titular = {'Goleiro': {'Nome': 'Vazio'}, 'Zagueiro Esquerdo': {'Status': 'Vazio'},
                            'Zagueiro Direito': {'Status': 'Vazio'},
                            'Lateral Esquerdo': {'Status': 'Vazio'}, 'Lateral Direito': {'Status': 'Vazio'},
                            'Meio-Campo 1': {'Status': 'Vazio'},
                            'Meio-Campo 2': {'Status': 'Vazio'}, 'Meio-Campo 3': {'Status': 'Vazio'},
                            'Meio-Campo 4': {'Status': 'Vazio'},
                            'Atacante Direito': {'Status': 'Vazio'}, 'Atacante Esquerdo': {'Status': 'Vazio'}}

    elif esquema_escolhido == 2:
        seu_time_titular = {
            'Goleiro': {'Status': 'Vazio'},
            'Zagueiro Esquerdo': {'Status': 'Vazio'},
            'Zagueiro Central 1': {'Status': 'Vazio'},
            'Zagueiro Central 2': {'Status': 'Vazio'},
            'Zagueiro Direito': {'Status': 'Vazio'},
            'Meio-Campo 1': {'Status': 'Vazio'},
            'Meio-Campo 2': {'Status': 'Vazio'},
            'Meio-Campo 3': {'Status': 'Vazio'},
            'Atacante Direito': {'Status': 'Vazio'},
            'Atacante Central': {'Status': 'Vazio'},
            'Atacante Esquerdo': {'Status': 'Vazio'}
        }

    elif esquema_escolhido == 3:

        seu_time_titular = {
            'Goleiro': {'Status': 'Vazio'},
            'Zagueiro Esquerdo': {'Status': 'Vazio'},
            'Zagueiro Central 1': {'Status': 'Vazio'},
            'Zagueiro Direito': {'Status': 'Vazio'},
            'Meio-Campo Esquerdo': {'Status': 'Vazio'},
            'Meio-Campo Central 1': {'Status': 'Vazio'},
            'Meio-Campo Central 2': {'Status': 'Vazio'},
            'Meio-Campo Central 3': {'Status': 'Vazio'},
            'Meio-Campo Direito': {'Status': 'Vazio'},
            'Atacante 1': {'Status': 'Vazio'},
            'Atacante 2': {'Status': 'Vazio'}
        }

    elif esquema_escolhido == 4:

        seu_time_titular = {
            'Goleiro': {'Status': 'Vazio'},
            'Zagueiro Esquerdo': {'Status': 'Vazio'},
            'Zagueiro Central 1': {'Status': 'Vazio'},
            'Zagueiro Central 2': {'Status': 'Vazio'},
            'Zagueiro Direito': {'Status': 'Vazio'},
            'Meio-Campo Defensivo 1': {'Status': 'Vazio'},
            'Meio-Campo Defensivo 2': {'Status': 'Vazio'},
            'Meio-Campo Central': {'Status': 'Vazio'},
            'Meio-Campo Esquerdo': {'Status': 'Vazio'},
            'Meio-Campo Direito ' : {'Status':'Vazio'},
            'Atacante': {'Status': 'Vazio'}
        }

    return seu_time_titular


#Funcao de escolha automatica do time titular de acrodo com o esquema tatico:
def escolha_automatica(seu_time):

    #Chamando funcoes para escolha do esquema:
    esquema_escolhido = escolha_esquema()
    seu_time_titular = esquemas_taticos(esquema_escolhido)


    #Incluindo o nome dos jogadores do time em uma lista para utilizar como validacao futuramente no codigo
    posicoes_preenchidas = list()
    jogadores_time = list()


    #Colocando o dicionario do jogador dentro do time titular:
    for posicao in seu_time:
        for key, value in posicao.items():
            for jogador in value:
                #Selecionando jogador da posicao correta para inserir:
                for posicao_vazia in seu_time_titular.keys():
                    if jogador['Posicao'] in posicao_vazia and jogador['Nome'] not in jogadores_time and posicao_vazia not in posicoes_preenchidas:
                        seu_time_titular[posicao_vazia] = jogador.copy()
                        #Colocando o jogador que ja esta no time em uma lista para nao repetir:
                        jogadores_time.append(jogador['Nome'])
                        posicoes_preenchidas.append((posicao_vazia))


    #Loop para preencher posicoes que ficaram vazias, se possivel:
    for pos in seu_time:
        for key2,value2 in pos.items():
            for jog in value2:
                #Analisando o jogador para inserir nas posicoes que faltam:
                for posicao_ainda_vazia in seu_time_titular.keys():
                    if jog['Posicao'] != 'Goleiro' and jog['Posicao'] not in posicao_ainda_vazia and jog['Nome'] not in jogadores_time and posicao_ainda_vazia not in posicoes_preenchidas:
                        seu_time_titular[posicao_ainda_vazia] = jog.copy()
                        # Colocando o jogador que ja esta no time em uma lista para nao repetir:
                        jogadores_time.append(jog['Nome'])
                        posicoes_preenchidas.append((posicao_ainda_vazia))



    return seu_time_titular


#Funcao para mostrar o time completo (tela inicial do jogo):
def mostrar_time(seu_time):
    print(f'{cor["fundo_preto"]}{'-' * 150}')
    mostra_nome_time()
    print(f'{cor["fundo_preto"]}{cor["azul"]}{"Jogadores":<20} {"Posicao":>20} {"Forca":>20}{"Idade":>20}{"Nacionalidade":>20}')  #Primeira linha da tabela
    print('-' * 150)

    for posicao in seu_time:    #Loop para mostrar o time formatado em tabela
        for key, value in posicao.items():
            for jogador in value:
                for caracteristica, valor in jogador.items():
                    print(f'{cor["verde"]}{valor:>20}', end='')
                print()


# Funcao que inclui o nome dos jogadores do time em uma lista para utilizar como validacao futuramente no codigo:
def lista_controle(seu_time):

    jogadores_time = list()
    for posicao in seu_time:
        for key, value in posicao.items():
            for jogador in value:
                jogadores_time.append(jogador['Nome'])

    return jogadores_time


#Funcao que inclui o nome dos jogadores do time titular em uma lista para utilizar como validacao futuramente no codigo:
def lista_controle_titulares(seu_time_titular):

    lista_titulares = list()
    for posicoes, jogadores in seu_time_titular.items():
        lista_titulares.append(jogadores['Nome'])

    return lista_titulares


#Funcao que relaciona o nome do jogador digitado com o dicionario correspondente:
def sistema_subs(seu_time,seu_time_titular,jogador_novo,jogador_velho):

    for posicao in seu_time:
        for key, lista in posicao.items():
            for jogador in lista:
                if jogador_novo == jogador['Nome']:
                    jogador_novo = jogador

    for pos, jog in seu_time_titular.items():
        if jogador_velho == jog['Nome']:
            jogador_velho = jog


    return jogador_novo,jogador_velho


#Funcao que realiza a substituicao utilizando como parametro o sistema de substituicao:
def realiza_subs(seu_time_titular,jogador_novo,jogador_velho):



    for key,jogador in seu_time_titular.items():
        if jogador['Nome'] == jogador_velho['Nome']:
            seu_time_titular[key] = jogador_novo

    return seu_time_titular


#Funcao que printa o nome do time formatado
def mostra_nome_time():
    with open("save.txt",'r') as file:
        nome_str = file.read()

    if nome_str == 'Flamengo':

        cor_time = cor["vermelho"]
    else:
        cor_time = cor["branco"]

    print(f'{cor["fundo_preto"]}{cor["negrito"]}{cor_time}{nome_str}{cor["limpa"]}')


#Funcao para mostrar o time titular:
def mostrando_time_titular(seu_time_titular):


    #Cabecalho principal:
    seu_time_titular = ajuste_forca(seu_time_titular)
    mostra_nome_time()
    print(f'{cor["fundo_preto"]}{cor["amarelo"]}{cor["negrito"]}{"TIME TITULAR"}{cor["limpa"]}')
    print(f'{cor["fundo_preto"]}{cor["amarelo"]}{'-' * 300}{cor["limpa"]}')
    print(f'{cor["fundo_preto"]}{cor["amarelo"]}{"Posicao no Esquema":<20}{"Jogadores":>20} {"Posicao":>20} {"Forca":>20}{"Idade":>20}{"Nacionalidade":>20}')
    print(f'{cor["fundo_preto"]}{cor["amarelo"]}{'-' * 300}{cor["limpa"]}')

    #Tabela:
    for item, value in seu_time_titular.items():
        print(f'{cor["fundo_preto"]}{cor["verde"]}{item:<20}', end='')
        for key, values in value.items():
            if value['fora_posicao']:
                value['fora_posicao'] = '   Fora da posicao correta'
                print(f'{cor["vermelho"]}{values:>20}',end='')

            else:
                value['fora_posicao'] = ''
                print(f'{cor["verde"]}{values:>20}', end='')
        print()
    print(f'{cor["limpa"]}')


#Funcao para mostrar o time reserva:
def mostrar_reservas(seu_time,seu_time_titular):
    seu_time_titular = ajuste_forca(seu_time_titular)
    titulares = lista_controle_titulares(seu_time_titular)
    todos = lista_controle(seu_time)
    banco_reservas = list()

    print(f'{cor["fundo_preto"]}{cor["amarelo"]}{'-' * 300}{cor["limpa"]}')
    print(F'{cor["fundo_preto"]}{cor["vermelho"]}{"BANCO DE RESERVAS":^5}')
    print(f'{cor["fundo_preto"]}{cor["vermelho"]}{"Jogadores":<20} {"Posicao":>20} {"Forca":>20}{"Idade":>20}{"Nacionalidade":>20}')  # Primeira linha da tabela
    print(f'{cor["fundo_preto"]}{cor["amarelo"]}{'-' * 300}{cor["limpa"]}')

    for posicao in seu_time:  # Loop para mostrar o time formatado em tabela
        for key, value in posicao.items():
            for jogador in value:
                if jogador['Nome'] not in titulares:
                    for caracteristica, valor in jogador.items():
                        print(f'{cor["fundo_preto"]}{cor["vermelho"]}{valor:>20}', end='')
                        banco_reservas.append(jogador)
                    print()
    print(f'{cor["limpa"]}')

    return banco_reservas


#Funcao para isolar o atributo da forca do time:
def forca_time(seu_time_titular):

    total = 0

    for jogador in seu_time_titular.values():
        total += jogador['Forca']


    return total

def mostra_forca(total_forca):
    print(f'{cor["fundo_preto"]}{cor["azul"]}Força do time: {total_forca}{cor["limpa"]}')


#Funcao que ajusta a forca do time de acordo com a posicao dos jogadores:
def ajuste_forca(seu_time_titular):

    for pos,jog in seu_time_titular.items():
        forca_original = jog['Forca']
        jog['fora_posicao'] = False
        if jog['Posicao'] not in pos:
            jog['Forca'] = forca_original - (jog['Forca'] - 20)
            jog['fora_posicao'] = True
            if jog['Forca'] < 0:
                jog['Forca'] = 0



    return seu_time_titular











#BLOCO 3 - INTERACOES COM USUARIO

#Menu principal onde as outras funcoes sao chamadas:
def menu_principal():

    seu_time,nome_time = escolha_time()
    salvar(nome_time)

    while True:
        print(f'{cor["fundo_preto"]}{cor['roxo']}','-'*100)
        escolha = str(input(f'{cor["fundo_preto"]}{cor["verde"]}[1] - {cor["roxo"]}Ver seu time\n{cor["verde"]}'
                            f'[2] - {cor["roxo"]}Escolher time titular (um por um)\n{cor["verde"]}'
                            f'[3] - {cor["roxo"]}Escolha automatica\n{cor["verde"]}'
                            f'[4] - {cor["roxo"]}Salvar Jogo\n{cor["verde"]}'
                            f'[5] - {cor["roxo"]}Music Menu{cor["limpa"]}\n'
                            f'> '))

        if escolha.isnumeric():
            ver = int(escolha)

            if 0 < ver < 6:


                if ver == 1:

                    mostrar_time(seu_time)


                elif ver == 2:

                    while True:
                        time_titular = escolhendo_posicao(seu_time)
                        time_titular = ajuste_forca(time_titular)
                        mostrando_time_titular(time_titular)
                        print('-'*100)
                        novamente = input(f'{cor["roxo"]}Deseja escolher novamente? [S] / [N]')

                        if novamente in 'Ss':
                            continue
                        elif novamente in 'Nn':
                            print('Time escolhido')
                            return time_titular,seu_time,nome_time

                elif ver == 3:

                    time_titular = escolha_automatica(seu_time)
                    mostrando_time_titular(time_titular)
                    return time_titular,seu_time,nome_time

                elif ver == 4:
                    salvar(nome_time)
                    print(f'{cor["azul"]}Jogo salvo.{cor["limpa"]}')

                elif ver == 5:
                    musica()

            else:
                print(f'{cor["vermelho"]}Digite um valor valido.{cor["limpa"]}')

        else:
            print(f'{cor["vermelho"]}Digite um valor valido.{cor["limpa"]}')


#Funcao para escolher esquemas taticos:
def escolha_esquema():

    while True:
        numero = 0
        esquema_escolhido = str(input(f'{cor["fundo_preto"]}{cor["verde"]}Deseja utilizar qual esquema tatico?\n'
                                      f'{cor["verde"]}[1]: {cor["roxo"]}4-4-2\n{cor["verde"]}[2]:{cor["roxo"]} 4-3-3\n{cor["verde"]}[3]: {cor["roxo"]}3-5-2\n{cor["verde"]}[4]: {cor["roxo"]}4-2-3-1\n: {cor["limpa"]}'))

        if esquema_escolhido.isnumeric():
            numero = int(esquema_escolhido)

        if 0 < numero < 5:
            return numero

        else:
            print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um numero de 1 a 4.{cor["limpa"]}')


#Funcao para montar o time que ira jogar, um por um:
def escolhendo_posicao(seu_time):

    jogadores_time = lista_controle(seu_time)

    #Formacao do time titular:
    escolha_sistema = escolha_esquema()
    seu_time_titular = esquemas_taticos(escolha_sistema)

    #Loop para captar o jogador por posicao:
    for posicao_vazia in seu_time_titular.keys():
        mostrar_time(seu_time)
        print('-'*100)

        #Loop para validar a entrada do usuario e garantir uma entrada valida para a posicao:
        while True:
            jogador_titular = input(f'{cor["fundo_preto"]}{cor["verde"]}Digite o nome do jogador para a posicao {posicao_vazia}: {cor["limpa"]}')
            print('-'*100)

            #Validando a entrada comparando com a lista de nomes dos jogadores do time:
            if jogador_titular in jogadores_time:

                #Colocando o dicionario do jogador dentro do time titular:
                for posicao in seu_time:
                    for key, value in posicao.items():
                        for jogador in value:
                            if jogador_titular in jogador.values():
                                seu_time_titular[posicao_vazia] = jogador

                #Removendo o jogador selecionado da lista de jogadores do time:
                jogadores_time.remove(jogador_titular)

                # Printando o time titular a cada entrada:
                print(f'{cor["amarelo"]}{cor["fundo_preto"]}TIME TITULAR{cor["limpa"]}')
                print('-' * 150)
                print(
                    f'{cor["fundo_preto"]}{cor["amarelo"]}{"Posicao no Esquema":<20}{"Jogadores":>20} {"Posicao":>20} {"Forca":>20}{"Idade":>20}{"Nacionalidade":>20}{cor["limpa"]}')
                print('-' * 150)

                for item, value in seu_time_titular.items():
                    print(f'{cor["fundo_preto"]}{cor["amarelo"]}{item:<20}', end='')
                    for key, values in value.items():
                        print(f'{cor["fundo_preto"]}{cor["amarelo"]}{values:>20}{cor["limpa"]}', end='')
                    print()
                break


            else:
                print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um nome valido.{cor["limpa"]}')


    return seu_time_titular


#Funcao para menu de substituicao de jogadores no time titular:
def substituicoes(seu_time,seu_time_titular):

    # Incluindo o nome dos jogadores do time em listas para utilizar como validacao futuramente no codigo
    lista_time = lista_controle(seu_time)
    lista_titulares = lista_controle_titulares(seu_time_titular)

    while True:
        substituir = str(input(f'{cor["fundo_preto"]}{cor["verde"]}Qual jogador deseja substituir?\n: '))

        if substituir in lista_time and substituir in lista_titulares:

            while True:
                escolha = int(input(f'{cor["verde"]}[1] - Escolher substituto para {substituir}\n{cor["vermelho"]}[2] - Voltar\n: '))



                if escolha == 1:

                    while True:
                        mostrar_time(seu_time)
                        print('-_-'*200)
                        print(f'{cor["amarelo"]}LISTA DE RESERVAS')
                        mostrar_reservas(seu_time,seu_time_titular)
                        substituto = str(input(f'{cor["amarelo"]}Nome do substituto: {cor["limpa"]}'))

                        if substituto in lista_time and substituto not in lista_titulares:
                            jogador_novo, jogador_velho = sistema_subs(seu_time,seu_time_titular,substituto,substituir)
                            seu_time_titular = realiza_subs(seu_time_titular,jogador_novo,jogador_velho)
                            seu_time_titular = ajuste_forca(seu_time_titular)
                            mostrando_time_titular(seu_time_titular)
                            return seu_time_titular




                        else:
                            print(f'{cor["vermelho"]}Digite um nome valido.{cor["limpa"]}')


                if escolha == 2:
                    break

                else:
                    print(f'{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')

        else:
            print(f'{cor["vermelho"]}Digite um nome valido..{cor["limpa"]}')










#Bloco 4 - Save and Load

#Save
def salvar(nome_time):

    save = open('save.txt','w')
    save.write(nome_time)
    save.close()
    return save


#Load
def load():
    with open("save.txt",'r') as file:
        seu_time = file.read()
    return seu_time









#BLOCO 5 - TESTES DE FUNCIONAMENTO DAS FUNCOES
def main():

    time_titular,seu_time,nome_time = menu_principal()
    forca = forca_time(time_titular)
    mostrar_reservas(seu_time,time_titular)
    mostra_forca(forca)


    while True:
        print('-'*100)
        print(f'{cor["fundo_preto"]}{cor["verde"]}{"MENU PRINCIPAL"}')
        escolha = str(input(f'[1] - {cor["roxo"]}Ver seu time completo\n{cor["verde"]}'
                            f'[2] - {cor["roxo"]}Ver seu time titular\n{cor["verde"]}'
                            f'[3] - {cor["roxo"]}Substituir\n'f'{cor["verde"]}'
                            f'[4] - {cor["roxo"]}Escolher esquema novamente\n{cor["verde"]}'
                            f'[5] -{cor["roxo"]} Salvar\n{cor["verde"]}'
                            f'[6] -{cor["roxo"]} Music Menu{cor["verde"]}\n'
                            f'[7] - {cor["roxo"]}Sair\n: {cor["limpa"]}'))

        if escolha.isnumeric():
            acao = int(escolha)

            if 0 < acao < 8:

                if acao == 1:
                    mostrar_time(seu_time)


                elif acao == 2:
                    mostrando_time_titular(time_titular)
                    mostra_forca(forca)
                    mostrar_reservas(seu_time, time_titular)

                elif acao == 3:
                    mostrando_time_titular(time_titular)
                    mostrar_reservas(seu_time,time_titular)
                    time_titular = substituicoes(seu_time,time_titular)
                    mostrando_time_titular(time_titular)

                elif acao == 4:
                    time_titular = escolha_automatica(seu_time)
                    mostrando_time_titular(time_titular)
                    forca = forca_time(time_titular)
                    mostrar_reservas(seu_time, time_titular)
                    mostra_forca(forca)

                elif acao == 5:
                    salvar(nome_time)
                    print(f'{cor["azul"]}Jogo salvo.{cor["limpa"]}')

                elif acao == 6:
                    musica()

                elif acao == 7:
                    print('Encerrando...')
                    break

                else:
                    print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')

        else:
            print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')




musica()
main()






