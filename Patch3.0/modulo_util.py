def calcula_salario(seu_time):

    valor_mercado = int
    # Formatando valor do jogador:
    for key, value in seu_time[0].items():
        for jogador in value:
            valor_mercado = jogador['Valor']
            cont_valor = 0
            valor_mercado = str(valor_mercado)

            for numero in valor_mercado:
                cont_valor += 1

            if cont_valor < 4:
                jogador['Valor_mostra'] = str(f'R$ {valor_mercado}')

            if cont_valor >= 4:
                if cont_valor == 4:
                    if valor_mercado[1] != '0':
                        jogador['Valor_mostra'] = str(f'R$ {valor_mercado[0]}.{valor_mercado[1]} mil')
                    else:
                        jogador['Valor_mostra'] = str(f'R$ {valor_mercado[0]} mil')
                elif cont_valor == 5:
                    jogador['Valor_mostra'] = str(f'R$ {valor_mercado[0]}{valor_mercado[1]} mil')
                elif cont_valor == 6:
                    jogador['Valor_mostra'] = str(f'R$ {valor_mercado[0]}{valor_mercado[1]}{valor_mercado[2]} mil')
                elif cont_valor == 7:
                    jogador['Valor_mostra'] = str(f'R$ {valor_mercado[0]}.{valor_mercado[1]} M')
                elif cont_valor == 8:
                    jogador['Valor_mostra'] = str(f'R$ {valor_mercado[0]}{valor_mercado[1]}.{valor_mercado[2]} M')
                elif cont_valor == 9:
                    jogador['Valor_mostra'] = str(f'R$ {valor_mercado[0]}{valor_mercado[1]}{valor_mercado[2]}.{valor_mercado[3]} M')


    #Formatando salario do jogado:
    for chave, valor in seu_time[0].items():

        #CALCULO SALARIO:
        for jogador in valor:
            valor_salario_bruto = 30000 + ((jogador['Valor']) *0.09)
            valor_salario_ajustado = int(valor_salario_bruto)
            jogador['Salario'] = valor_salario_ajustado
            salario_mostra = str(jogador['Salario'])

            cont_salario = 0

            for numero in salario_mostra:
                cont_salario += 1
            if cont_salario < 4:
                jogador['Salario_mostra'] = str(f'R$ {salario_mostra}')

            if cont_salario >= 4:
                if cont_salario == 4:
                    if salario_mostra[1] != '0':
                        jogador['Salario_mostra'] = str(f'R$ {salario_mostra[0]}.{salario_mostra[1]} mil')
                    else:
                        jogador['Salario_mostra'] = str(f'R$ {salario_mostra[0]} mil')
                elif cont_salario == 5:
                    jogador['Salario_mostra'] = str(f'R$ {salario_mostra[0]}{salario_mostra[1]} mil')
                elif cont_salario == 6:
                    jogador['Salario_mostra'] = str(f'R$ {salario_mostra[0]}{salario_mostra[1]}{salario_mostra[2]} mil')
                elif cont_salario == 7:
                    jogador['Salario_mostra'] = str(f'R$ {salario_mostra[0]}.{salario_mostra[1]} M')
                elif cont_salario == 8:
                    jogador['Salario_mostra'] = str(f'R$ {salario_mostra[0]}{salario_mostra[1]}.{salario_mostra[2]} M')
                elif cont_salario == 9:
                    jogador['Salario_mostra'] = str(f'R$ {salario_mostra[0]}{salario_mostra[1]}{salario_mostra[2]}.{salario_mostra[3]} M')




    return seu_time


def mecanica_energia(seu_time):

    for key, value in seu_time[0].items():
        for jogador in value:
            if jogador['Energia'] < 0:
                jogador['Energia'] = 0

    return seu_time




