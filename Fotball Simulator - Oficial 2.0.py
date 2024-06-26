from random import choice
from random import randint
from time import sleep

def print_sleep(text):
    print(text)
    sleep(1)

def times():
    # Display dos times para o usuario:

    times_brasil = ['Flamengo', '* * * * *',
                    'Corinthans', '* * * *',
                    'Palmeiras', '* * * * *',
                    'Fluminense', '* * * *'
        , 'Botafogo', ' * * *',
                    'Vasco', '* * *',
                    'Athletico Paranaense', '* * * *',
                    'Santos', '* * * *',
                    'Cruzeiro', '* * *',
                    'Atletico Mineiro', '* * * *',
                    'Gremio', '* * * *',
                    'Internacional', '* * * *',
                    'Redbull Bragantino', '* * *',
                    'Sao Paulo', '* * * *',
                    'America Mineiro', '* * *',
                    'Bahia', '* * *']

    times_argentina = ['Boca Juniors', '* * * *',
                       'River Plate', '* * * * *',
                       'Racing', '* * *',
                       'Estudiantes', '* * * *',
                       'Independiente', '* * * *',
                       'San Lorenzo', '* * * *',
                       'Huracán', '* *',
                       'Rosario Central', '* * *',
                       'Newell`s Old Boys', '* * *',
                       'Vélez Sarsfield', '* * *',
                       'Lanús', '* *',
                       'Banfield', '*',
                       'Argentinos Juniors', '*',
                       'Talleres', '*',
                       'Colón', '*',
                       'Godoy Cruz', '*',
                       'Unión', '*',
                       'Central Córdoba', '*',
                       'Aldosivi', '*',
                       'Arsenal de Sarandí', '*',
                       'Platense', '*',
                       'Sarmiento', '*',
                       'Defensa y Justicia', '*'
                       ]

    times_colombia = [
        'Atlético Nacional', '* * * * *',
        'Millonarios', '* * * *',
        'América de Cali', '* * *',
        'Deportivo Cali', '* * *',
        'Independiente Santa Fe', '* * *',
        'Junior', '* * *',
        'Once Caldas', '* *',
        'Deportes Tolima', '* *',
        'Atlético Junior', '*',
        'Cúcuta Deportivo', '*',
        'Envigado', '*',
        'Patriotas Boyacá', '*',
        'Alianza Petrolera', '*',
        'Jaguares de Córdoba', '*',
        'Boyacá Chicó', '*',
        'Rionegro Águilas', '*',
        'La Equidad', '*',
        'Atlético Bucaramanga', '*',
        'Deportivo Pasto', '*',
        'Águilas Doradas', '*'
    ]

    times_uruguai = [
        'Nacional', '* * * * *',
        'Peñarol', '* * * * *',
        'Defensor Sporting', '* * *',
        'Danubio', '* * *',
        'Montevideo Wanderers', '* *',
        'River Plate', '* *',
        'Cerro', '* *',
        'Progreso', '* *',
        'Liverpool', '* *',
        'Boston River', '*',
        'Plaza Colonia', '*',
        'Fénix', '*',
        'Cerro Largo', '*',
        'Deportivo Maldonado', '*',
        'Rentistas', '*',
        'Torque', '*',
        'Villa Española', '*',
        'Deportivo Colonia', '*',
        'Rampla Juniors', '*'
    ]

    # Lista dos tiers dos times para o algoritimo:

    tier1 = [
        'Flamengo',  # Brasil
        'Palmeiras',  # Brasil
        'River Plate',  # Argentina
        'Atletico Mineiro',  # Brasil
        'Nacional',  # Uruguai
        'Peñarol'  # Uruguai
    ]
    tier2 = [
        'Corinthans',  # Brasil
        'Fluminense',  # Brasil
        'Boca Juniors',  # Argentina
        'Independiente',  # Argentina
        'Estudiantes',  # Argentina
        'Athletico Paranaense',  # Brasil
        'Gremio',  # Brasil
        'Internacional',  # Brasil
        'Sao Paulo',  # Brasil
        'San Lorenzo',  # Argentina
        'Huracán',  # Argentina
        'Rosario Central',  # Argentina
        'Newell\'s Old Boys',  # Argentina
        'Vélez Sarsfield',  # Argentina
        'Lanús',  # Argentina
        'Banfield',  # Argentina
        'Argentinos Juniors',  # Argentina
        'Talleres',  # Argentina
        'Colón',  # Argentina
        'Godoy Cruz',  # Argentina
        'Unión',  # Argentina
        'Central Córdoba',  # Argentina
        'Aldosivi',  # Argentina
        'Arsenal de Sarandí',  # Argentina
        'Platense',  # Argentina
        'Sarmiento',  # Argentina
        'Defensa y Justicia'  # Argentina
    ]

    tier3 = [
        'Racing',  # Argentina
        'Cruzeiro',  # Brasil
        'Redbull Bragantino',  # Brasil
        'Botafogo',  # Brasil
        'Vasco',  # Brasil
        'Santos',  # Brasil
        'America Mineiro',  # Brasil
        'Bahia',  # Brasil
        'Atlético Nacional',  # Colômbia
        'Millonarios',  # Colômbia
        'América de Cali',  # Colômbia
        'Deportivo Cali',  # Colômbia
        'Independiente Santa Fe',  # Colômbia
        'Junior',  # Colômbia
        'Once Caldas',  # Colômbia
        'Deportes Tolima',  # Colômbia
        'Atlético Junior',  # Colômbia
        'Cúcuta Deportivo',  # Colômbia
        'Envigado',  # Colômbia
        'Patriotas Boyacá',  # Colômbia
        'Alianza Petrolera',  # Colômbia
        'Jaguares de Córdoba',  # Colômbia
        'Boyacá Chicó',  # Colômbia
        'Rionegro Águilas',  # Colômbia
        'La Equidad',  # Colômbia
        'Atlético Bucaramanga',  # Colômbia
        'Deportivo Pasto',  # Colômbia
        'Águilas Doradas',  # Colômbia
        'Danubio',  # Uruguai
        'Montevideo Wanderers',  # Uruguai
        'Cerro',  # Uruguai
        'Progreso',  # Uruguai
        'Liverpool',  # Uruguai
        'Boston River',  # Uruguai
        'Plaza Colonia',  # Uruguai
        'Fénix',  # Uruguai
        'Cerro Largo',  # Uruguai
        'Deportivo Maldonado',  # Uruguai
        'Rentistas',  # Uruguai
        'Torque',  # Uruguai
        'Villa Española',  # Uruguai
        'Deportivo Colonia',  # Uruguai
        'Rampla Juniors'  # Uruguai
    ]

    # Lista com todos os times para o campeonato:

    lista_geral = [times_brasil] + [times_argentina] + [times_colombia] + [times_uruguai]

    return times_brasil, times_argentina, times_uruguai, times_colombia, tier1, tier2, tier3, lista_geral

def acrecimos():
    return randint(1,10)

def escolha_time(times_brasil,times_argentina,times_uruguai,times_colombia):

    while True:
        country = input('Escolha o pais:\n[1] - Times Brasil\n[2] - Times Argentina\n'
                        '[3] - Times Colombia\n[4] - Times Uruguai\n: ')
        if country == '1':
            print('-_-'*40)
            print('TIMES BRASIL - TIME / RANKING')

            while True:

                for times in times_brasil:

                    if times_brasil.index(times) % 2 == 0:
                        print (f'{times:.<40}',end = '')
                    else:
                        print(f'{times:>5}')



                time = input(f'Escolha um time: ')
                if time in times_brasil:
                    return time
                else:
                    print('Digite o time que quer escolher.')

        elif country == '2':

            while True:
                print('-_-' * 40)
                print('TIMES ARGENTINA - TIME / RANKING')
                for times in times_argentina:

                    if times_argentina.index(times) % 2 == 0:
                        print(f'{times:.<40}', end='')
                    else:
                        print(f'{times:>5}')

                time = input(f'Escolha um time: ')
                if time in times_argentina:
                    return time
                else:
                    print('Digite o nome do time que deseja escolher.')

        elif country == '3':
            print('-_-' * 40)
            print('TIMES COLOMBIA - TIME / RANKING')

            while True:

                for times in times_colombia:

                    if times_colombia.index(times) % 2 == 0:
                        print(f'{times:.<40}', end='')
                    else:
                        print(f'{times:>5}')

                time = input(f'Escolha um time: ')
                if time in times_colombia:
                    return time
                else:
                    print('Digite o time que quer escolher.')


        elif country == '4':
            print('-_-' * 40)
            print('TIMES URUGUAI - TIME / RANKING')

            while True:

                for times in times_uruguai:

                    if times_uruguai.index(times) % 2 == 0:
                        print(f'{times:.<40}', end='')
                    else:
                        print(f'{times:>5}')

                time = input(f'Escolha um time: ')
                if time in times_uruguai:
                    return time
                else:
                    print('Digite o time que quer escolher.')

        else:
            print('Digite o numero da escolha.')

def time_pc(m,v,time_casa):

    lista = ['Flamengo', 'Corinthans', 'Palmeiras', 'Fluminense', 'Boca Juniors',
             'River Plate', 'Racing','Botafogo','Vasco','Athletico Paranaense','Santos'
                    ,'Cruzeiro','Atletico Mineiro','Gremio','Internacional','Redbull Bragantino',
             'Estudiantes','Independiente','Sao Paulo','America Mineiro','Bahia']

    while True:
        y = input('-_-_-_-_-_-MODO DE JOGO-_-_-_-_-_-\n[1] - Escolher adversario\n[2] - Amistoso com time aleatorio\n[3] - Campeonato Mata-Mata\n[4] - Escolher time novamente\n: ')
        if y == '1':
            time_fora = escolha_time(times_brasil,times_argentina,times_colombia,times_uruguai)
            if time_fora == time_casa:
                print('Escolha outro time.')
                time_fora = escolha_time(times_brasil,times_argentina,times_colombia,times_uruguai)
            return time_fora
        elif y == '2':
            time_fora = choice(lista)
            while time_fora == time_casa:
                time_fora = choice(lista)
            return time_fora
        elif y == '3':
            times_sorteados = sorteio_campeonato(time_casa,times_brasil,times_argentina,times_uruguai,times_colombia)
            campeonato(m, v, p1, times_sorteados, times_brasil, times_argentina, times_uruguai, times_colombia)

        elif y == '4':
            time_casa = escolha_time(times_brasil,times_argentina,times_colombia,times_uruguai)
            time_pc(m,v,time_casa)
            continue

        else:
            print('Digite 1 ou 2.')

def jogo(time_casa, time_fora):
    tier1 = [
        'Flamengo',  # Brasil
        'Palmeiras',  # Brasil
        'River Plate',  # Argentina
        'Atletico Mineiro',  # Brasil
        'Nacional',  # Uruguai
        'Peñarol'  # Uruguai
    ]
    tier2 = [
        'Corinthans',  # Brasil
        'Fluminense',  # Brasil
        'Boca Juniors',  # Argentina
        'Independiente',  # Argentina
        'Estudiantes',  # Argentina
        'Athletico Paranaense',  # Brasil
        'Gremio',  # Brasil
        'Internacional',  # Brasil
        'Sao Paulo',  # Brasil
        'San Lorenzo',  # Argentina
        'Huracán',  # Argentina
        'Rosario Central',  # Argentina
        'Newell\'s Old Boys',  # Argentina
        'Vélez Sarsfield',  # Argentina
        'Lanús',  # Argentina
        'Banfield',  # Argentina
        'Argentinos Juniors',  # Argentina
        'Talleres',  # Argentina
        'Colón',  # Argentina
        'Godoy Cruz',  # Argentina
        'Unión',  # Argentina
        'Central Córdoba',  # Argentina
        'Aldosivi',  # Argentina
        'Arsenal de Sarandí',  # Argentina
        'Platense',  # Argentina
        'Sarmiento',  # Argentina
        'Defensa y Justicia'  # Argentina
    ]
    tier3 = [
        'Racing',  # Argentina
        'Cruzeiro',  # Brasil
        'Redbull Bragantino',  # Brasil
        'Botafogo',  # Brasil
        'Vasco',  # Brasil
        'Santos',  # Brasil
        'America Mineiro',  # Brasil
        'Bahia',  # Brasil
        'Atlético Nacional',  # Colômbia
        'Millonarios',  # Colômbia
        'América de Cali',  # Colômbia
        'Deportivo Cali',  # Colômbia
        'Independiente Santa Fe',  # Colômbia
        'Junior',  # Colômbia
        'Once Caldas',  # Colômbia
        'Deportes Tolima',  # Colômbia
        'Atlético Junior',  # Colômbia
        'Cúcuta Deportivo',  # Colômbia
        'Envigado',  # Colômbia
        'Patriotas Boyacá',  # Colômbia
        'Alianza Petrolera',  # Colômbia
        'Jaguares de Córdoba',  # Colômbia
        'Boyacá Chicó',  # Colômbia
        'Rionegro Águilas',  # Colômbia
        'La Equidad',  # Colômbia
        'Atlético Bucaramanga',  # Colômbia
        'Deportivo Pasto',  # Colômbia
        'Águilas Doradas',  # Colômbia
        'Danubio',  # Uruguai
        'Montevideo Wanderers',  # Uruguai
        'Cerro',  # Uruguai
        'Progreso',  # Uruguai
        'Liverpool',  # Uruguai
        'Boston River',  # Uruguai
        'Plaza Colonia',  # Uruguai
        'Fénix',  # Uruguai
        'Cerro Largo',  # Uruguai
        'Deportivo Maldonado',  # Uruguai
        'Rentistas',  # Uruguai
        'Torque',  # Uruguai
        'Villa Española',  # Uruguai
        'Deportivo Colonia',  # Uruguai
        'Rampla Juniors'  # Uruguai
    ]

    if time_casa in tier1 and time_fora in tier2:
        gol = randint(0, 500)
        gol_fora = randint(0, 1000)
        cartao_amarelo_casa = randint(0, 1000)
        cartao_amarelo_fora = randint(0,600)
        cartao_vermelho_casa = randint(0, 1500)
        cartao_vermelho_fora = randint(0,600)
        penalti = randint(0, 500)

    elif time_casa in tier1 and time_fora in tier3:
        gol = randint(0, 500)
        gol_fora = randint(0, 2000)
        cartao_amarelo_casa = randint(0, 1000)
        cartao_amarelo_fora = randint(0,600)
        cartao_vermelho_casa = randint(0, 1500)
        cartao_vermelho_fora = randint(0,600)
        penalti = randint(0, 500)

    elif time_casa in tier2 and time_fora in tier3:
        gol = randint(0, 500)
        gol_fora = randint(0, 2500)
        cartao_amarelo_casa = randint(0, 1000)
        cartao_amarelo_fora = randint(0,600)
        cartao_vermelho_casa = randint(0, 1500)
        cartao_vermelho_fora = randint(0,600)
        penalti = randint(0, 500)


    elif time_casa and time_fora in tier1 or time_casa and time_fora in tier2 or time_casa and time_fora in tier3:
        gol = randint(0, 1000)
        gol_fora = randint(0, 1000)
        cartao_amarelo_casa = randint(0, 1000)
        cartao_amarelo_fora = randint(0,600)
        cartao_vermelho_casa = randint(0, 1500)
        cartao_vermelho_fora = randint(0,600)
        penalti = randint(0, 500)


    if gol < gol_fora*0.01:
        return 'gol'
    elif gol_fora < gol*0.01:
        return 'gol_fora'
    elif cartao_amarelo_casa < 5:
        return 'cartao_amarelo_casa'
    elif cartao_vermelho_casa < 3:
        return 'cartao_vermelho_casa'
    elif cartao_amarelo_fora < 5:
        return 'cartao_amarelo_fora'
    elif cartao_vermelho_fora < 3:
        return 'cartao_vermelho_fora'
    elif penalti < 2:
        return 'penalti_casa'
    elif penalti > 498:
        return 'penalti_fora'

def sorteio_campeonato(p1,times_brasil,times_argentina,times_uruguai,times_colombia):

    print('Campeonato mata-mata!')
    times_sorteados = [p1]

    #Removendo o ranking das listas de times para sobrar apenas o nome dos times:

    for contador,time in enumerate(times_brasil):
        if '*' in time:
            times_brasil.remove(time)

    for contador,time in enumerate(times_argentina):
        if '*' in time:
            times_argentina.remove(time)

    for contador,time in enumerate(times_uruguai):
        if '*' in time:
            times_uruguai.remove(time)

    for contador,time in enumerate(times_colombia):
        if '*' in time:
            times_colombia.remove(time)


    # Sorteando os times


    #Sorteando 2 times de cada pais para o campeonato:

    for n in range(0, 4):
        time_sorteado = choice(times_brasil)
        times_sorteados.append(time_sorteado)

    for n in range(0, 4):
        time_sorteado = choice(times_argentina)
        times_sorteados.append(time_sorteado)

    for n in range(0, 4):
        time_sorteado = choice(times_uruguai)
        times_sorteados.append(time_sorteado)

    for n in range(0, 4):
        time_sorteado = choice(times_colombia)
        times_sorteados.append(time_sorteado)




    for time in times_sorteados:

        repetidos = times_sorteados.count(time)

        if repetidos > 1:
            times_sorteados.remove(time)
            time = choice(times_brasil)
            while time in times_sorteados:
                time = choice(times_brasil)
            times_sorteados.append(time)

    for time2 in lista_geral:

        repetidos2 = times_sorteados.count(time2)
        if repetidos2 > 1:
            times_sorteados.remove(time2)
            time2 = choice(times_argentina)
            while time2 in times_sorteados:
                time2 = choice(times_argentina)
            times_sorteados.append(time2)


        return times_sorteados

def campeonato(m, v, p1, times_sorteados, times_brasil, times_argentina, times_uruguai, times_colombia):

    lista_participantes = times_brasil + times_argentina + times_uruguai + times_colombia

    trofeu = ("""
               ___________
              '._==_==_=_.'
              .-\:      /-.
             | (|:.     |) |
              '-|:.     |-'
                \::.    /
                 '::. .'
                   ) (
                 _.' '._
                `"""""""`
    """)

    # Verificando se algum time esta repetido:

    for time in times_sorteados:
        repetido = times_sorteados.count(time)
        if repetido > 1:
            times_sorteados.remove(time)
            time = choice(times_brasil)

    i = 1

    # Mostrando os jogos

    print('-_-' * 25)
    print('SORTEIO PARA AS OITAVAS DE FINAL')
    print('-_-' * 25)
    for c in range(0, 8):
        if c == 0:
            print(f'Jogo {c + 1}: {times_sorteados[c]}  x  {times_sorteados[c + 1]}')
        elif c > 0:
            print(f'Jogo {c + 1}: {times_sorteados[c * 2]}  x  {times_sorteados[c + (i + 1)]}')
            i += 1


    # INICIO CAMPEONATO

    while True:

        iniciar = input('[1] - Sortear novamente\n[2] - Iniciar\n: ')

        # EXECUCAO DOS JOGOS
        if iniciar == '1':
            times_sorteados = sorteio_campeonato(p1, times_brasil, times_argentina, times_uruguai, times_colombia)
            campeonato(m, v, p1, times_sorteados, times_brasil, times_argentina, times_uruguai, times_colombia)


        elif iniciar == '2':
            vencedor1 = Prog(m, v, p1, times_sorteados[1])
            vencedor2, gol_p1j1, gol_pcj1 = jogo_simulacao(times_sorteados[2], times_sorteados[3],tier1,tier2,tier3)
            vencedor3, gol_p1j2, gol_pcj2 = jogo_simulacao(times_sorteados[4], times_sorteados[5],tier1,tier2,tier3)
            vencedor4, gol_p1j3, gol_pcj3 = jogo_simulacao(times_sorteados[6], times_sorteados[7],tier1,tier2,tier3)
            vencedor5, gol_p1j4, gol_pcj4 = jogo_simulacao(times_sorteados[8], times_sorteados[9],tier1,tier2,tier3)
            vencedor6, gol_p1j5, gol_pcj5 = jogo_simulacao(times_sorteados[10], times_sorteados[11],tier1,tier2,tier3)
            vencedor7, gol_p1j6, gol_pcj6 = jogo_simulacao(times_sorteados[12], times_sorteados[13],tier1,tier2,tier3)
            vencedor8, gol_p1j7, gol_pcj7 = jogo_simulacao(times_sorteados[14], times_sorteados[15],tier1,tier2,tier3)

            # PLACAR DOS JOGOS OITAVAS DE FINAL
            if vencedor1 == p1:
                print('Placar dos outros jogos:')
                print('-_-' * 30)
                print(f'{times_sorteados[2]}:{gol_p1j1}\n{times_sorteados[3]}:{gol_pcj1}')
                print('--' * 30)
                print(f'{times_sorteados[4]}:{gol_p1j2}\n{times_sorteados[5]}:{gol_pcj2}')
                print('--' * 30)
                print(f'{times_sorteados[6]}:{gol_p1j3}\n{times_sorteados[7]}:{gol_pcj3}')
                print('--' * 30)
                print(f'{times_sorteados[8]}:{gol_p1j4}\n{times_sorteados[9]}:{gol_pcj4}')
                print('--' * 30)
                print(f'{times_sorteados[10]}:{gol_p1j5}\n{times_sorteados[11]}:{gol_pcj5}')
                print('--' * 30)
                print(f'{times_sorteados[12]}:{gol_p1j6}\n{times_sorteados[13]}:{gol_pcj6}')
                print('--' * 30)
                print(f'{times_sorteados[14]}:{gol_p1j7}\n{times_sorteados[15]}:{gol_pcj7}')
                print('--' * 30)
                sleep(1)
                print(
                    f'Quartas de final:\n{vencedor1} x {vencedor2}\n{vencedor3} x {vencedor4}\n{vencedor5} x {vencedor6}\n{vencedor7} x {vencedor8}')

                # QUARTAS DE FINAL

                while True:
                    print('-_-' * 25)
                    print('QUARTAS DE FINAL')
                    print('-_-' * 25)
                    semi = input('Aperte enter para continuar.')

                    if semi == '':
                        semi_finalista1 = Prog(m, v, vencedor1, vencedor2)
                        semi_finalista2, gol_p1_quartas, gol_pc_quartas = jogo_simulacao(vencedor3, vencedor4,tier1,tier2,tier3)
                        semi_finalista3, gol_p1_quartas2, gol_pc_quartas2 = jogo_simulacao(vencedor5, vencedor6,tier1,tier2,tier3)
                        semi_finalista4, gol_p1_quartas3, gol_pc_quartas3 = jogo_simulacao(vencedor7, vencedor8,tier1,tier2,tier3)

                        # SEMI-FINAIS

                        if semi_finalista1 == vencedor1:
                            print('Placar dos outros jogos:')
                            print('--' * 30)
                            print(f'{vencedor3}:{gol_p1_quartas}\n{vencedor4}:{gol_pc_quartas}')
                            print('--' * 30)
                            print(f'{vencedor5}:{gol_p1_quartas2}\n{vencedor6}:{gol_pc_quartas2}')
                            print('--' * 30)
                            print(f'{vencedor7}:{gol_p1_quartas3}\n{vencedor8}:{gol_pc_quartas3}')
                            print('--' * 30)
                            print(f'Semi-Finalistas:\n{semi_finalista1} x {semi_finalista2}')
                            print('--' * 30)
                            print(f'{semi_finalista3} x {semi_finalista4}')
                            print('--' * 30)
                            sleep(2)
                            print('Semi-Final')

                            while True:
                                semi_final = input('Aperte enter para continuar.')

                                if semi_final == '':
                                    finalista1 = Prog(m, v, semi_finalista1, semi_finalista2)
                                    finalista2, gol_p1_semi, gol_pc_semi = jogo_simulacao(semi_finalista3,
                                                                                          semi_finalista3,tier1,tier2,tier3)

                                    if finalista1 == semi_finalista1:
                                        print('Parabens! Voce chegou na grande final!')
                                        print('-_-' * 30)
                                        # FINAL
                                        while True:
                                            final = input('Aperte enter para continuar.')

                                            if final == '':
                                                campeao = Prog(m, v, finalista1, finalista2)
                                                if campeao == finalista1:
                                                    print('PARABENS, VOCE FOI CAMPEAO!!!!')
                                                    print(trofeu)
                                                else:
                                                    print('Vice campeao!')

                                                    while True:
                                                        derrota = input(
                                                            '[1] - Jogar novamente\n[2] - Voltar ao menu principal')

                                                        if derrota == '1':
                                                            times_sorteados = sorteio_campeonato(p1, times_brasil,
                                                                                                 times_argentina,
                                                                                                 times_uruguai,
                                                                                                 times_colombia)
                                                            campeonato(m, v, p1, times_sorteados, times_brasil, times_argentina, times_uruguai, times_colombia)

                                                        elif derrota == '2:':
                                                            velocidade_jogo = float(input(
                                                                'Velocidade do jogo:\n1 = Normal\n0.5 = Rapido\n0.25 = Muito Rapido\n3 ou mais = Muito Lento\n: '))
                                                            min = acrecimos()
                                                            p1 = escolha_time(times_brasil, times_argentina,
                                                                              times_colombia, times_uruguai)
                                                            pc = time_pc(min, velocidade_jogo, p1)
                                                            Prog(min, velocidade_jogo, p1, pc)
                                                        else:
                                                            print('Entrada invalida.')
                                    else:
                                        print('Eliminado na semi-final')
                                        while True:
                                            derrota = input(
                                                '[1] - Jogar novamente\n[2] - Voltar ao menu principal')

                                            if derrota == '1':
                                                times_sorteados = sorteio_campeonato(p1, times_brasil,
                                                                                     times_argentina,
                                                                                     times_uruguai,
                                                                                     times_colombia)
                                                campeonato(m, v, p1, times_sorteados, times_brasil, times_argentina,
                                                           times_uruguai, times_colombia)

                                            elif derrota == '2:':
                                                velocidade_jogo = float(input(
                                                    'Velocidade do jogo:\n1 = Normal\n0.5 = Rapido\n0.25 = Muito Rapido\n3 ou mais = Muito Lento\n: '))
                                                min = acrecimos()
                                                p1 = escolha_time(times_brasil, times_argentina,
                                                                  times_colombia, times_uruguai)
                                                pc = time_pc(min, velocidade_jogo, p1)
                                                Prog(min, velocidade_jogo, p1, pc)
                                            else:
                                                print('Entrada invalida.')


                            else:
                                print('Entrada invalida.')

                    # ELIMINADO QUARTAS
                    else:
                        print('Fim de jogo, eliminado nas quartas de final.')
                        while True:

                            derrota = input('[1] - Jogar novamente\n[2] - Voltar ao menu principal\n: ')

                            if derrota in '1':
                                times_sorteados = sorteio_campeonato(p1, times_brasil, times_argentina, times_uruguai,
                                                                     times_colombia)
                                campeonato(m, v, p1, times_sorteados, times_brasil, times_argentina, times_uruguai, times_colombia)

                            elif derrota in '2:':
                                velocidade_jogo = float(input(
                                    'Velocidade do jogo:\n1 = Normal\n0.5 = Rapido\n0.25 = Muito Rapido\n3 ou mais = Muito Lento\n: '))
                                min = acrecimos()
                                p1 = escolha_time(times_brasil, times_argentina, times_colombia, times_uruguai)
                                pc = time_pc(min, velocidade_jogo, p1)
                                Prog(min, velocidade_jogo, p1, pc)

        # ELIMINADO OITAVAS
        else:
            print('Fim de jogo, eliminado nas oitavas de final.')
            while True:
                derrota = input('[1] - Jogar novamente\n[2] - Sair do jogo\n: ')
                if derrota == '1':
                    velocidade_jogo = float(input(
                        'Velocidade do jogo:\n1 = Normal\n0.5 = Rapido\n0.25 = Muito Rapido\n3 ou mais = Muito Lento\n: '))
                    min = acrecimos()
                    p1 = escolha_time(times_brasil, times_argentina, times_colombia, times_uruguai)
                    pc = time_pc(min, velocidade_jogo, p1)
                    Prog(min, velocidade_jogo, p1, pc)
                elif derrota == '2':
                    print('Encerrando o programa...')
                    sleep(2)
                    break
                break


def jogo_simulacao(p1,pc,tier1,tier2,tier3):

    if p1 in tier1:
        chances_p1 = (0,0,0,0,0,0,0,0,
                      1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,
                      2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,5,5,6)
    if p1 in tier2:
        chances_p1 = (0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,2, 2, 2, 2, 2, 2, 2, 2, 2,
                      2, 2, 2, 2, 2, 2, 3, 3, 3, 3)

    if p1 in tier3:
        chances_p1 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3)

    if pc in tier1:
        chances_pc = (0, 0, 0, 0, 0, 0, 0, 0,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                      2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6)

    if pc in tier2:
        chances_pc = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                      2, 2, 2, 2, 2, 2, 3, 3, 3, 3)

    if pc in tier3:
        chances_pc = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3)


    gol_p1 = choice(chances_p1)
    gol_pc = choice(chances_pc)

    while gol_pc == gol_p1:
        gol_p1 = (choice(chances_p1) + randint(0,1))
        gol_pc = (choice(chances_pc) + randint(0,1))

    if gol_p1 > gol_pc:
        return p1, gol_p1, gol_pc

    elif gol_pc > gol_p1:
        return pc, gol_p1, gol_pc

def intervalo(p1,pc,gol_casa,gol_fora,cartao_a_casa,cartao_a_fora,cartao_v_casa,cartao_v_fora,jogadores_p1,jogadores_pc,infos_gols):
    print('-_-'*20)
    print(f'{'INTERVALO DO JOGO':>40}')
    print('-_-'*20)

    #Calculo posse de bola
    posse_total = 100

    if gol_casa > gol_fora and cartao_a_casa < cartao_a_fora and cartao_v_casa < cartao_v_fora and jogadores_p1 == jogadores_pc:
        posse_casa = (posse_total - randint(40,55))
        posse_fora = 100 - posse_casa

        if jogadores_p1 < jogadores_pc:
            perde = randint(0,10)
            posse_casa -= perde
            posse_fora += perde

    elif gol_casa < gol_fora and cartao_a_casa > cartao_a_fora and cartao_v_casa > cartao_v_fora and jogadores_p1 == jogadores_pc:

        posse_casa = (posse_total - randint(40, 55))
        posse_fora = 100 - posse_casa

        if jogadores_p1 > jogadores_pc:
            perde = randint(0, 10)
            posse_casa += perde
            posse_fora -= perde

    else:

        posse_casa = (posse_total - randint(40, 55))
        posse_fora = 100 - posse_casa


    #Calculo chutes a gol:

    chute_casa = gol_casa + randint(4,10)
    chute_fora = gol_fora + randint(4,10)



    while True:
        mostrar = input('[1] - Estatisticas do jogo\n[2] - Voltar ao jogo\n: ').strip()

        if mostrar in '1':
            print('-_-'*200)
            print(f'                 {p1} [{gol_casa}]----------------[{gol_fora}]  {pc}')

            if gol_casa > 0:
                print('-_-'*200)
                print(f'Gols do {p1}:')
                for c in range(0,len(infos_gols[0])):
                    print(f'Gol aos {infos_gols[0][c]} min`')
                print('-_-'*200)

            if gol_fora > 0:
                print('-_-' * 200)
                print(f'Gols do {pc}:')
                for c in range (0,len(infos_gols[1])):
                    print(f'Gol aos {infos_gols[1][c]} min`')
                print('-_-' * 200)

            print(f'Posse de bola:       {posse_casa}%-----------------------{posse_fora}%')
            print(f'Chutes a gol:        {chute_casa}-------------------------{chute_fora}')
            print(f'Cartoes amarelos:    {cartao_a_casa}-------------------------{cartao_a_fora}')
            print(f'Cartoes vermelhos:   {cartao_v_casa}-------------------------{cartao_v_fora}')
            print('-_-' * 200)

        elif mostrar in '2':
            break

        else:
            print('Digite 1 ou 2.')

def Prog(m, x, p1, pc):

    #Variaveis:

    gol_casa = gol_fora = cartao_a_casa = cartao_a_fora = cartao_v_casa = cartao_v_fora = expulsos_casa = expulsos_fora = 0
    jogadores_p1 = 11
    jogadores_p2 = 11

    #Frases que aparecem no jogo:

    lista_frases_chute_errado = ['Isolou a bola!', 'Meu deus, que fase! Escorregou e errou o chute.',
                                 'Chutou fraco em cima do goleiro...']
    lista_frases_gols = ['Camisa 9 chutou de fora da area e fez um golaco!', 'Meu deus, que fase! Gol contra!',
                         'Gol de cabeca!', 'Golaco de falta!', 'Gol depois de linda tabela entra os atacantes!',
                         'Falha incrivel da defesa, atacante nao perdoou!']

    minutos_gol = []
    min_gols_time_casa = []
    min_gols_time_fora = []

    #Inicio do jogo:

    print(f'Jogo: {p1} x {pc}')

    #Definicao dos dois tempos:

    for d in range(0, 2):

        if d == 0:
            t = 'Primeiro tempo'

        elif d == 1:
            t = 'Segundo tempo'
            print('Fim do primeiro tempo.')
            minutos_gol.append(min_gols_time_casa)
            minutos_gol.append(min_gols_time_fora)
            sleep(x)
            print(f'Placar:\n{p1} - {gol_casa}\n{pc} - {gol_fora}')
            intervalo(p1,pc,gol_casa,gol_fora,cartao_a_casa,cartao_a_fora,cartao_v_casa,cartao_v_fora,jogadores_p1,jogadores_p2,minutos_gol)
            sleep(x)
            print('Inicio do segundo tempo!')
            sleep(4)

    #Inicio do jogo minuto a minuto:

        for c in range(1, 45 + m):
            frase_chute_errado = choice(lista_frases_chute_errado)
            frase_gol = choice(lista_frases_gols)

            print(f'{c}`min ')
            sleep(x)
            acao = jogo(p1, pc)

        #Acoes durante o jogo:

            if acao == 'gol':
                gol_casa += 1
                print(f'{frase_gol}', end=' ')
                print(f'Gol do {p1} aos {c}min do {t}!\n{p1}: {gol_casa}\n{pc}: {gol_fora}')
                min_gols_time_casa.append(c)


            elif acao == 'gol_fora':
                gol_fora += 1
                print(f'{frase_gol}', end=' ')
                print(f'Gol do {pc} aos {c}min do {t}!\n{p1}: {gol_casa}\n{pc}: {gol_fora}\n {c}`min.')
                min_gols_time_fora.append(c)


            elif jogadores_p1 > jogadores_p2:
                chance_gol = randint(0,500)
                if chance_gol < 5:
                    gol_casa += 1
                    print(f'{frase_gol}', end=' ')
                    print(f'Gol do {p1} aos {c}min do {t}!\n{p1}: {gol_casa}\n{pc}: {gol_fora}')
                    min_gols_time_casa.append(c)


            elif jogadores_p2 > jogadores_p1:
                chance_gol = randint(0,500)
                if chance_gol < 5:
                    gol_fora += 1
                    print(f'{frase_gol}', end=' ')
                    print(f'Gol do {pc} aos {c}min do {t}!\n{p1}: {gol_casa}\n{pc}: {gol_fora}')
                    min_gols_time_fora.append(c)

            elif acao == 'cartao_amarelo_casa':
                cartao_a_casa += 1
                print(f'Falta feia! Cartao amarelo para o jogador do {p1}')
                if cartao_a_casa > 1 and cartao_a_casa % 2 == 0:
                    print(f'Dois cartoes amarelos. Jogador do {p1} expulso aos {c}` min.')
                    expulsos_casa += 1
                    jogadores_p1 -= 1
                    cartao_v_casa +=1

            elif acao == 'cartao_vermelho_casa':
                cartao_v_casa += 1
                expulsos_casa += 1
                print(f'Falta criminosa! Cartao vermelho. Jogador do {p1} expulso aos {c}` min.')
                jogadores_p1 -= 1

            elif expulsos_casa > 4:
                print(f'Jogo encerrado por W.O, quatro jogadores expulsos. Vitoria do {pc}')
                break

            elif acao == 'cartao_amarelo_fora':
                cartao_a_fora += 1
                print(f'Falta feia! Cartao amarelo para o jogador do {pc}')
                if cartao_a_fora > 1 and cartao_a_fora % 2 == 0:
                    print(f'Dois cartoes amarelos. Jogador do {pc} expulso aos {c}` min.')
                    expulsos_fora += 1
                    jogadores_p2 -= 1
                    cartao_v_fora += 1

            elif acao == 'cartao_vermelho_fora':
                cartao_v_fora += 1
                expulsos_fora += 1
                jogadores_p2 -= 1
                print(f'Falta criminosa! Cartao vermelho. Jogador do {pc} expulso aos {c}` min.')

            elif expulsos_fora > 4:
                print(f'Jogo encerrado por W.O, quatro jogadores expulsos. Vitoria do {p1}')
                break

            elif acao == 'penalti_casa':

                penal = randint(0, 300)

                if penal < 150:
                    gol_casa += 1
                    print(f'PRIII! O juiz apita para a marca de penalti para o {p1}!')
                    sleep(2)
                    print('Jogador vai para a bola.')
                    sleep(1)
                    print('Ele bate forte e...')
                    sleep(1)
                    print(f'Goooooool! Placar:\n{p1}: {gol_casa}\n{pc}: {gol_fora}')
                    min_gols_time_casa.append(c)

                else:
                    print(f'PRIII! O juiz apita para a marca de penalti para o {p1}!')
                    sleep(2)
                    print('Jogador vai para a bola.')
                    sleep(1)
                    print('Ele bate forte e...')
                    sleep(1)
                    print('Bateu mal pra caramba, bola pra fora!')

            elif acao == 'penalti_fora':
                penal = randint(0, 300)
                if penal < 150:
                    gol_fora += 1
                    print(f'PRIII! O juiz apita para a marca de penalti para o {pc}!')
                    sleep(2)
                    print('Jogador vai para a bola.')
                    sleep(1)
                    print('Ele bate forte e...')
                    sleep(1)
                    print(f'Goooooool! Placar:\n{p1}: {gol_casa}\n{pc}: {gol_fora}')
                    min_gols_time_fora.append(c)

                else:
                    print(f'PRIII! O juiz apita para a marca de penalti para o {pc}!')
                    sleep(2)
                    print('Jogador vai para a bola.')
                    sleep(1)
                    print('Ele bate forte e...')
                    sleep(1)
                    print(f'{frase_chute_errado}!')


            elif c == 45:
                print(f'Acrecimos: {c} + {m - 1} min')

    sleep(2)
    print(f'Placar:\n{p1}:{gol_casa}\n{pc}:{gol_fora}')
    if gol_casa > gol_fora:
        print(f'Vitoria do {p1}')
        print('-_-'*30)
        return p1
    elif gol_casa < gol_fora:
        print(f'Vitoria do {pc}')
        print('-_-' *30)
        return pc

    else:
        print('Empate!')
        sleep(x)
        print('Disputa de penaltis!')
        vencedor = disputa_penaltis(p1,pc)
        return vencedor

def disputa_penaltis(p1,pc):

    #Penaltis - p1
    batidas_p1 = 0
    gols_p1 = 0


    #Penaltis - p2
    batidas_pc = 0
    gols_pc = 0

    # Chute a Chute
    acertos_p1 = []
    acertos_pc = []
    batida_certa_p1 = batida_certa_pc = '0'
    batida_errada_p1 = batida_errada_pc = 'X'

    for chutes in range(0, 11):

        chance_gol = randint(0, 100)
        sleep(2)

        print('-_-'*50)

        if chutes % 2 == 0:
            batidas_p1 += 1

            if chance_gol > 50:
                print(f'Jogador do {p1} vai para a bola...')
                sleep(2)
                print('Bate forte e....')
                sleep(2)
                gols_p1 += 1
                acertos_p1.append(batida_certa_p1)
                print(f'GOl do {p1}!')
                print(f'{p1}: {acertos_p1}')
                print(f'{pc}: {acertos_pc}')

            else:
                print(f'Jogador do {p1} vai para a bola...')
                sleep(2)
                print('Bate forte e....')
                sleep(2)
                acertos_p1.append(batida_errada_p1)
                print(f'Jogador do {p1} errou!')
                print(f'{p1}: {acertos_p1}')
                print(f'{pc}: {acertos_pc}')


        else:
            batidas_pc += 1

            if chance_gol > 50:
                print(f'Jogador do {pc} vai para a bola...')
                sleep(2)
                print('Bate forte e....')
                sleep(2)
                gols_pc += 1
                print(f'Gol do {pc}!')
                acertos_pc.append(batida_certa_pc)
                print(f'{p1}: {acertos_p1}')
                print(f'{pc}: {acertos_pc}')


            else:
                print(f'Jogador do {pc} vai para a bola...')
                sleep(2)
                print('Bate forte e....')
                sleep(2)
                print(f'Jogador do {pc} chutou pra fora!')
                acertos_pc.append(batida_errada_pc)
                print(f'{p1}: {acertos_p1}')
                print(f'{pc}: {acertos_pc}')


        #Condicoes de vitoria

        if batidas_p1 and batidas_pc <= 5:

            if batidas_pc >= 3 and gols_p1 >= 3 and gols_pc < 1:
                return p1

            if batidas_p1 >= 3 and gols_pc >= 3 and gols_p1 < 1:
                return pc

            if batidas_pc >= 4 and gols_p1 >= 4 and gols_pc <= 2:
                return p1

            if batidas_p1 >= 4 and gols_pc >= 4 and gols_p1 <= 2:
                return pc

            if batidas_p1 >=4 and batidas_pc >=4:
                if gols_p1 > gols_pc:
                    return p1

                elif gols_pc > gols_p1:
                    return pc


print('-_-'*50)
print(f'{'FOOTBALL SIMULATOR':>80}')
print('-_-'*50)
times_brasil,times_argentina,times_colombia,times_uruguai, tier1, tier2, tier3, lista_geral = times()
velocidade_jogo = float(input('*****Velocidade do jogo*****\n[1] = Normal\n[0.5] = Rapido\n[0.25] = Muito Rapido\n[3] ou mais = Muito Lento\n: '))
min = acrecimos()
p1 = escolha_time(times_brasil,times_argentina,times_colombia,times_uruguai)
pc = time_pc(min,velocidade_jogo,p1)
Prog(min,velocidade_jogo,p1,pc)

