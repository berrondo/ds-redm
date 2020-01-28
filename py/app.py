from datetime import date, timedelta
from collections import OrderedDict
from csv import DictReader
from itertools import chain
from operator import add
from pprint import pprint

from copy import deepcopy

from auxs import status_finais, status_em_ordem, tercas, oscila, WEEKDAY, status_atelier, status_fabrica, INSERT, into, \
    finalizadas

SEQUENCIA = {}
HISTORIA = {}
JOURNAL = {}
# xxx = OrderedDict()

with open('journals7.csv', newline='', encoding="utf8") as f:
    reader = DictReader(f)
    for row in reader:
        demanda = int(row['demanda'])
        criacao = row['criacao']
        data_de_criacao = date(*map(int, criacao[:11].split('-')))
        data_e_hora = row['em']
        data = date(*map(int, data_e_hora[:11].split('-')))
        de = row['de'] or "DESCONHECIDO"
        status = row['para'] or "SEM_DESTINO"

        if data_de_criacao in JOURNAL:
            if demanda not in JOURNAL[data_de_criacao]:
                JOURNAL[data_de_criacao][demanda] = {'de': 'Novo', 'para': 'Novo'}
        else:
            JOURNAL[data_de_criacao] = {demanda: {'de': 'Novo', 'para': 'Novo'}}

        JOURNAL[data] = JOURNAL.get(data, {})
        JOURNAL[data][demanda] = JOURNAL[data].get(demanda, {'de': de})
        JOURNAL[data][demanda]['para'] = status

        # xxx[data_e_hora] = xxx.get(data_e_hora, {})
        # xxx[data_e_hora][demanda] = xxx[data_e_hora].get(data_e_hora, {})
        # xxx[data_e_hora][demanda]['de'] = de
        # xxx[data_e_hora][demanda]['para'] = status

        # SEQUENCIA[demanda] = SEQUENCIA.get(demanda, ['Novo', de]) + [status]
        #
        # HISTORIA[demanda] = HISTORIA.get(demanda, {})
        # if data_de_criacao not in HISTORIA[demanda]:
        #     HISTORIA[demanda][data_de_criacao] = ('Novo', 'Novo')
        # # HISTORIA[demanda][data_e_hora] = de, status
        # HISTORIA[demanda][data] = JOURNAL[data][demanda]['de'], status


def traz_o_dia_anterior(quadro, quadro_ontem, hoje):
    for status in quadro_ontem.keys():
        quadro[hoje] = quadro.get(hoje, {})
        quadro[hoje][status] = quadro_ontem[status][:]

def move_de_para(quadro, demanda_de_para, hoje):
    falhas_em_remove_de = []
    for demanda, de_para in demanda_de_para.items():
        de = de_para['de']
        para = de_para['para']
        quadro[hoje] = quadro.get(hoje, {de: [], para: []})

        # quadro hoje remove demanda de:
        try:
            # while demanda in quadro[hoje][de]:
            quadro[hoje][de].remove(demanda)
        except (ValueError, KeyError):
            falhas_em_remove_de.append((demanda, de, para))

        # quadro hoje append demanda para:
        quadro[hoje][para] = quadro[hoje].get(para, [])
        if demanda not in quadro[hoje][para]:
            quadro[hoje][para].append(demanda)

        # # desacumuladas...
        # if para in status_finais:
        #     status_desacumulado = 'HOJE ' + para
        #     quadro[hoje][status_desacumulado] = quadro[hoje].get(status_desacumulado, [])
        #     if demanda not in quadro[hoje][status_desacumulado]:
        #         quadro[hoje][status_desacumulado].append(demanda)

    if falhas_em_remove_de:
        corrige(falhas_em_remove_de, quadro[hoje])

def corrige(falhas_em_remove_de, quadro_hoje):
    for demanda, de, para in falhas_em_remove_de:
        for status, demandas in quadro_hoje.items():
            if status != para and demanda in demandas:
                if status not in status_finais:
                    demandas.remove(demanda)
                elif para in status_finais:
                    demandas.remove(demanda)

D = sorted(JOURNAL.items())
ontem, demanda_de_para_ontem = D[0]
QUADRO = OrderedDict()
move_de_para(QUADRO, demanda_de_para_ontem, ontem)

for data, demanda_de_para in D[1:]:
    traz_o_dia_anterior(QUADRO, QUADRO[ontem], data)
    move_de_para(QUADRO, demanda_de_para, data)
    ontem = data

def valida():
    ## validando QUADRO:
    for data, statuses in sorted(QUADRO.items()):
        ## demands em mais de um status no mesmo dia:
        todos_os_statuses_do_dia = list(chain(statuses))
        if len(todos_os_statuses_do_dia) != len(set(todos_os_statuses_do_dia)):
            print(data)
            # exit()
            ## demanda repetida no status:
            for status in status_em_ordem:
                try:
                    demandas = statuses[status]
                    if len(demandas) != len(set(demandas)):
                        print(demandas)
                        # exit()
                except KeyError:
                    continue

def por_status():
    S = {}
    SS= {}
    T = {}
    for demanda, statuses in SEQUENCIA.items():
        str_statuses = '->'.join(statuses)
        S[str_statuses] = S.get(str_statuses, []) + [demanda]

        set_statues = ' > '.join(OrderedDict().fromkeys(statuses, None).keys())
        SS[set_statues] = SS.get(set_statues, []) + [demanda]

        for status in set(statuses):
            T[status] = T.get(status, 0) + 1
    print(len(S))
    print(len(SS))
    print(len(SEQUENCIA))
    print(len(JOURNAL))
    pprint(T)

def desacumula_e_agrega():
    QUADRO_DESACUMULADO = deepcopy(QUADRO)
    statuses_ontem = list(QUADRO.values())[0]
    for data, statuses in QUADRO.items():
        for status in statuses:
            ## desacumula
            if status in status_finais:
                status_desacumulado = 'HOJE '+status
                QUADRO_DESACUMULADO[data][status_desacumulado] = list(set(statuses[status]) - set(statuses_ontem.get(status, [])))
        statuses_ontem = statuses
    return QUADRO_DESACUMULADO
# QUADRO = desacumula_e_agrega()

datas_no_quadro = list(QUADRO.keys())
with open('out2.txt', 'w') as o:
    # for data, statuses in sorted(QUADRO.items()):
    #     print(INSERT.format(*(into[k] for k in into), data, *(len(statuses.get(k, [])) for k in into)), file=o)
    # exit()

    finalizadas_ate_aqui = 0
    for terca in tercas:
        total_fabrica = 0
        total_atelier = 0
        finalizadas_totais = 0
        data = terca
        statuses = {}

        osc = oscila()
        while terca > datas_no_quadro[0]:
            print()
            try:
                statuses = QUADRO[terca]
                break
            except KeyError:
                print(terca, end=' ')
                terca = data - timedelta(days=osc.__next__())
                print(terca)

        print(terca, WEEKDAY[terca.weekday()], file=o)

        # for status, demandas in statuses.items():
        for status in status_em_ordem:
            try:
                demandas = statuses[status]
                qt_demandas = len(demandas)
                #
                if status in status_finais:
                    finalizadas_totais += qt_demandas
                if status in status_atelier:
                    total_atelier += qt_demandas
                if status in status_fabrica:
                    total_fabrica = qt_demandas
                #
                if demandas:
                    print('\t',
                          '%-4d ' % qt_demandas,
                          # '%-4d ' % len(set(demandas)),
                          status,
                          # '\n\t\t', demandas,
                          file=o)
            except KeyError:
                # print(status)
                continue
        finalizadas_no_periodo = finalizadas_totais - finalizadas_ate_aqui
        if total_fabrica:
            print('\t %-4d  = FABRICA' % (total_fabrica+total_atelier), file=o)
        if total_atelier and not total_fabrica:
            print('\t %-4d  = ATELIER' % total_atelier, file=o)
        print('\t %-4d  = CONCLUIDAS' % finalizadas(statuses), file=o)
        finalizadas_ate_aqui = finalizadas_totais


        # for k, v in sorted(JOURNAL.items()):
        #     print(k, file=o)
        #     for kk, vv in v.items():
        #         print('\t', '%-8s' % kk, '%-51s' % vv['de'], '-> ', vv['para'], file=o)

        # for k, v in sorted(HISTORIA.items()):
        #     print(k, file=o)
        #     for kk, vv in v.items():
        #         print('\t', '%-19s' % kk, ' ', '%-51s' % vv[0], '-> ', vv[1], file=o)

        # for k, v in sorted(SEQUENCIA.items()):
        #     print(k, v, file=o)

        # for k, v in sorted(S.items()):
        #     print('%-3s ' % str(len(v)), k, '\n\t  ', v, file=o)

        # for k, v in sorted(SS.items()):
        #     print('%-3s ' % str(len(v)), k, '\n\t  ', v, file=o)

