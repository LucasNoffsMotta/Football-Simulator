import cores

cor=cores.cores()

def financas(seu_time):
    # Calcula Salario:
    financas = dict()
    salarios = 0
    for key, jog in seu_time[0].items():
        for jogador in jog:
            salarios += jogador['Salario']
            financas['Salarios'] = salarios

    return financas


def formata_numero(numero):
    numero_mostra = str(numero)
    cont_valor = 0

    for numero in numero_mostra:
        cont_valor += 1

    if cont_valor < 4:
        return str(f'R$ {numero_mostra}')

    if cont_valor >= 4:
        if cont_valor == 4:
            if numero_mostra != '0':
                return str(f'R$ {numero_mostra[0]}.{numero_mostra[1]} mil')
            else:
                return str(f'R$ {numero_mostra[0]} mil')
        elif cont_valor == 5:
            return str(f'R$ {numero_mostra[0]}{numero_mostra[1]} mil')
        elif cont_valor == 6:
            return str(f'R$ {numero_mostra[0]}{numero_mostra[1]}{numero_mostra[2]} mil')
        elif cont_valor == 7:
            return str(f'R$ {numero_mostra[0]}.{numero_mostra[1]} M')
        elif cont_valor == 8:
            return str(f'R$ {numero_mostra[0]}{numero_mostra[1]}.{numero_mostra[2]} M')
        elif cont_valor == 9:
            return str(
                f'R$ {numero_mostra[0]}{numero_mostra[1]}{numero_mostra[2]}.{numero_mostra[3]} M')


def tabela_financeira(seu_time):
    financas_dict = financas(seu_time)
    financas_dict['Compras'] = 0
    financas_dict['Vendas'] = 0
    total_despesas = financas_dict['Compras'] + financas_dict['Salarios']
    total_ganhos = financas_dict['Vendas']
    saldo_final = total_ganhos - total_despesas

    salario_formatado = formata_numero(financas_dict['Salarios'])
    compras_formatado = formata_numero(financas_dict['Compras'])
    vendas_formatado = formata_numero(financas_dict['Vendas'])
    total_despesas_formatado = formata_numero(total_despesas)
    total_ganhos_formatado = formata_numero(total_ganhos)
    saldo_final_formatado = formata_numero(saldo_final)


    print(f'{cor["fundo_preto"]}{cor["amarelo"]}{cor["negrito"]}')
    print('-'*160)
    print('R$  -  FINANCAS -  R$')
    print('-' * 150)
    print(f'{cor["limpa"]}{cor["fundo_preto"]}')
    print(f'{cor["amarelo"]}{"Total Salarios:"}{cor["verde"]}\t{salario_formatado}')
    print(f'{cor["amarelo"]}{"Total Compras:"}{cor["verde"]}\t{compras_formatado}')
    print(f'{cor["amarelo"]}{"Total Vendas:"}{cor["verde"]}\t{vendas_formatado}')
    print('-'*150)
    print(f'{cor["vermelho"]}{"Total despesas:"}{cor["vermelho"]}\t{total_despesas_formatado}')
    print(f'{cor["verde"]}{"Total ganhos:"}\t{total_ganhos_formatado}')
    if saldo_final > 0:
        print(f'{cor["amarelo"]}{"Saldo final:"}{cor["verde"]}\t{saldo_final_formatado}')
    else:
        print(f'{cor["amarelo"]}{"Saldo final:"}{cor["vermelho"]}\t{saldo_final_formatado}')
    print('-' * 150)

