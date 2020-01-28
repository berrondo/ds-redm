from collections import OrderedDict
from csv import DictReader
from pprint import pprint

from auxs import status_em_ordem

SEQUENCIA = {}
HISTORIA = {}
JOURNAL = {}

with open('journals3.csv', newline='', encoding="utf8") as f:
    reader = DictReader(f)
    for row in reader:
        demanda = int(row['demanda'])
        criacao = row['criacao']
        data_de_criacao = criacao[:11]
        data_e_hora = row['em']
        data = data_e_hora[:11]
        status = row['para'] or "SEM_DESTINO"

        if data_de_criacao in JOURNAL:
            if demanda not in JOURNAL[data_de_criacao]:
                JOURNAL[data_de_criacao][demanda] = {'para': 'Novo'}
        else:
            JOURNAL[data_de_criacao] = {demanda: {'para': 'Novo'}}

        JOURNAL[data] = JOURNAL.get(data, {})
        JOURNAL[data][demanda] = JOURNAL[data].get(demanda, {})
        JOURNAL[data][demanda]['para'] = status

        SEQUENCIA[demanda] = SEQUENCIA.get(demanda, ['Novo']) + [status]

        HISTORIA[demanda] = HISTORIA.get(demanda, {})
        if data_de_criacao not in HISTORIA[demanda]:
            HISTORIA[demanda][data_de_criacao] = 'Novo'
        HISTORIA[demanda][data] = status


def traz_o_dia_anterior(quadro, quadro_ontem, hoje):
    for status in quadro_ontem.keys():
        quadro[hoje] = quadro.get(hoje, {})
        quadro[hoje][status] = quadro_ontem[status]

def move_de_para(quadro, demanda_para, hoje):
    for demanda, de_para in demanda_para.items():
        para = de_para['para']
        quadro[hoje] = quadro.get(hoje, {para: []})
        quadro[hoje][para] = quadro[hoje].get(para, [])[:]

        if demanda not in quadro[hoje][para]:
            quadro[hoje][para].append(demanda)

        for status, demandas in quadro[hoje].items():
            if status != para and demanda in demandas:
                demandas.remove(demanda)


D = sorted(JOURNAL.items())
ontem, demanda_e_para_ontem = D[0]
QUADRO = OrderedDict()
move_de_para(QUADRO, demanda_e_para_ontem, ontem)

for data, demanda_para in D[1:]:
    traz_o_dia_anterior(QUADRO, QUADRO[ontem], data)
    move_de_para(QUADRO, demanda_para, data)
    ontem = data


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


with open('out22.txt', 'w') as o:
    for data, statuses in sorted(QUADRO.items()):
        print(data, file=o)
        for s in status_em_ordem:
            try:
                demandas = statuses[s]
                if demandas:
                    print('\t',
                          '%-4d ' % len(demandas),
                          s,
                          # '\n\t\t', demandas,
                          file=o)
            except KeyError:
                continue

    for k, v in sorted(JOURNAL.items()):
        print(k, file=o)
        for kk, vv in v.items():
            print('\t', '%-7s' % kk, '-> ', vv['para'], file=o)

    for k, v in sorted(HISTORIA.items()):
        print(k, file=o)
        for kk, vv in v.items():
            print('\t', '%-12s' % kk, ' ', '-> ', vv, file=o)

    for k, v in sorted(SEQUENCIA.items()):
        print(k, v, file=o)

    for k, v in sorted(S.items()):
        print('%-3s ' % str(len(v)), k, '\n\t  ', v, file=o)

    for k, v in sorted(SS.items()):
        print('%-3s ' % str(len(v)), k, '\n\t  ', v, file=o)

