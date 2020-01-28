import datetime
from datetime import date

t1 = date(2013, 3, 5)  # print(t1.weekday())  # no nosso caso basta comecar em 20/5
h = datetime.date.today()

tercas = [date.fromordinal(i) for i in range(t1.toordinal(), h.toordinal(), 7)]

WEEKDAY = {
    0: 'SEG',
    1: 'TER',
    2: 'QUA',
    3: 'QUI',
    4: 'SEX',
    5: 'SAB',
    6: 'DOM',
}

def oscila(i=0):
    while True:
        i += 1
        yield i
        yield i * -1

def finalizadas(dia_no_quadro):
    total = 0
    for status, demandas in dia_no_quadro.items():
        if status.startswith('HOJE'):
            total += len(demandas)
    return total

todos_os_status = (
    'Novo',
    'Dividir em sprints',

    'Realizar orçamento',
    'Validar orçamento',
    'Especificar testes',
    'Validar especificação/testes',
    'Realizar implementação',
    'Testar implementação',
    'Homologar com Demandante',
    'Validar artefatos',
    'Entregar artefatos',
    'Atualizar registro da demanda',

    'Demanda concluída com ônus',
    'Demanda com ônus em pontos de função concluída',

    'Desenvolver internamente',
    'Validar com a Área Demandante',
    'Demanda sem ônus em pontos de função concluída',
    'Demanda concluída sem ônus',

    'Demanda cancelada',
    '',

    ## Defeito
    # 'Avaliar defeito',
    # 'Decidir sobre o defeito',
    # 'Fechado',

    # 'Concluído',
    # 'Reavaliação', 'Rejeição cancelada',
    # 'Aceito',

    ## PDTI
    # 'Iniciado',
    # 'Pendente',
    # 'Cancelado',

    ## Fábrica
    # 'Preparar documentação para fábrica',
    # 'Pronto para fábrica',

    # 'Estimar pontos de função',
    # 'Elaborar parecer: desenvolver ou adquirir?',
    # 'Análise e decisão pela Divisão de Sistemas',
    # 'Elaborar e consolidar doc técnica, formal e OS',
    # 'Considerar decisão da DISIS: ratificar ou retificar',
    # 'Realizar reunião de planejamento',
    # 'Aprovar ordem de serviço'
    # 'Priorizar funcionalidades com o cliente',
    # 'Verificar e empenhar saldo de PFs',
    # 'Elaborar product backlog',

    # 'Elaborar procedimento para homologação',
    # 'Realizar implantação no ambiente de homologação',
    # 'Disponível para teste',
    # 'Executar manutenção',
    # 'Implantar em produção',

    # 'Contar pontos de função',
    # 'Complementar documentação para contagem',

    # 'Detalhar Projeto (Proc. implant. SW adquirido externamente)',
)

status_atelier = (
    'Realizar orçamento', 'Validar orçamento',
    'Especificar testes', 'Validar especificação/testes',
    'Realizar implementação',
    'Testar implementação', 'Homologar com Demandante',
    'Validar artefatos', 'Entregar artefatos',
    'Atualizar registro da demanda',
)

status_fabrica = (
    # Defeito
    'Avaliar defeito', 'Decidir sobre o defeito', 'Fechado',

    ## DBA ?
    # 'Concluído',    'Reavaliação', 'Rejeição cancelada',    'Aceito',

    ## PDTI
    # 'Iniciado',    'Pendente',    'Cancelado',

    # Fábrica
    'Preparar documentação para fábrica', 'Pronto para fábrica',

    'Estimar pontos de função', 'Elaborar parecer: desenvolver ou adquirir?',
    'Análise e decisão pela Divisão de Sistemas', 'Elaborar e consolidar doc técnica, formal e OS',
    'Considerar decisão da DISIS: ratificar ou retificar', 'Realizar reunião de planejamento',
    'Aprovar ordem de serviço'    'Priorizar funcionalidades com o cliente',
    'Verificar e empenhar saldo de PFs', 'Elaborar product backlog',

    'Elaborar procedimento para homologação', 'Realizar implantação no ambiente de homologação',
    'Disponível para teste', 'Executar manutenção',
    'Implantar em produção',

    'Contar pontos de função', 'Complementar documentação para contagem',

    'Detalhar Projeto (Proc. implant. SW adquirido externamente)',
)

status_finais = ('Demanda concluída sem ônus', 'Demanda concluída com ônus', 'Demanda cancelada',
                 'Demanda sem ônus em pontos de função concluída', 'Demanda com ônus em pontos de função concluída',
                 )
antigos_status_finais = ('Demanda concluída sem ônus', 'Demanda concluída com ônus', 'Demanda cancelada',
                         'Demanda sem ônus em pontos de função concluída',
                         'Demanda com ônus em pontos de função concluída',
                         'Fechado', 'Cancelado',
                         # 'Concluído' ????
                         'Aceito'
                         )

fluxo_interno = (
'Novo', 'Desenvolver internamente', 'Validar com a Área Demandante', 'Demanda sem ônus em pontos de função concluída',
'Demanda com ônus em pontos de função concluída', 'Demanda cancelada')

status_em_ordem = (
    'Novo',
    'Dividir em sprints',

    '[SISCAP] Em Análise',
    'Desenvolver internamente',
    'Validar com a Área Demandante',

    'Preparar documentação para fábrica',
    'Pronto para fábrica',

    'Estimar pontos de função',
    'Elaborar parecer: desenvolver ou adquirir?',
    'Análise e decisão pela Divisão de Sistemas',

    'Detalhar Projeto (Proc. implant. SW adquirido externamente)',

    'Elaborar e consolidar doc técnica, formal e OS',
    'Considerar decisão da DISIS: ratificar ou retificar',
    'Priorizar funcionalidades com o cliente',
    'Elaborar product backlog',

    'Realizar orçamento',
    'Validar orçamento',
    'Especificar testes',
    'Validar especificação/testes',

    'Realizar implementação',
    'Executar manutenção',
    'Testar implementação',

    'Elaborar procedimento para homologação',
    'Realizar implantação no ambiente de homologação',
    'Disponível para teste',

    'Homologar com Demandante',

    'Entregar artefatos',
    'Validar artefatos',

    'Contar pontos de função',
    'Complementar documentação para contagem',

    'Atualizar registro da demanda',

    'Demanda concluída com ônus',
    'Demanda concluída sem ônus',
    'Demanda cancelada',
    'Demanda com ônus em pontos de função concluída',
    'Demanda sem ônus em pontos de função concluída',

    # 'Reavaliação',
    # 'Aceito',
    #
    # 'Avaliar defeito',
    # 'Decidir sobre o defeito',
    # 'Fechado',
    #
    # 'Iniciado',
    # 'Pendente',
    # 'Cancelado',
)

diferencas = {
    'Demanda sem ônus em pontos de função concluída':
        {15749, 11277, 17935, 13328, 2577, 4119, 3736, 6937, 20766, 5919, 3745, 14262, 15673, 11194, 11195, 7232, 2881,
         2244, 4689, 4178, 11735, 13016, 2779, 11229, 11230, 2013, 9057, 5345, 4459, 11249, 11250, 1915, 2428},
    'Demanda com ônus em pontos de função concluída':
        {17422, 19854, 14360, 15387, 15390, 17198, 1596, 73, 77, 78, 79, 80, 81, 82, 83, 20948, 86, 88, 91, 92, 93, 94,
         95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 2927, 115, 122},
    'Demanda cancelada':
        {1156, 14090, 8974, 12695, 4635, 15390, 23415, 3887, 14262, 4792, 3447, 22336, 18242, 3400, 13520, 11605, 11734,
         11735, 19544, 14186, 5111, 23414, 11127, 23416}
}

into = {
    'Novo': 'novo',
    'Dividir em sprints': 'dividir_em_sprints',

    'Desenvolver internamente': 'desenvolver_internamente',
    'Validar com a Área Demandante': 'validar_com_area_demandante',

    'Realizar orçamento': 'realizar_orcamento',
    'Validar orçamento': 'validar_orcamento',
    'Especificar testes': 'especificar_testes',
    'Validar especificação/testes': 'validar_especificacao_testes',
    'Realizar implementação': 'realizar_implementacao',
    'Testar implementação': 'testar_implementacao',
    'Homologar com Demandante': 'homologar_com_demandante',
    'Entregar artefatos': 'entregar_artefatos',
    'Validar artefatos': 'validar_artefatos',
    'Atualizar registro da demanda': 'atualizar_registro_da_demanda',

    'HOJE Demanda cancelada': 'demanda_cancelada',
    'HOJE Demanda concluída com ônus': 'demanda_concluida_com_onus',
    'HOJE Demanda concluída sem ônus': 'demanda_concluida_sem_onus',
}
INSERT = """INSERT INTO totais_nos_status (data, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}) VALUES ('{} 23:59:00', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});"""
