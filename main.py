import pandas as pd
from maquina import *
from of import *
from produto import *
from slot import *
from import_files import *
from functions import *

import_ofs()
import_slots()
import_maquinas()

definir_capacidades()

for index in range(len(ofs)):
    ofs[index].definir_data_min()
#     print(ofs[index].data_min)

id_ofs=get_ids(ofs)

ofs_ret=filter_ofs('RETIFICADORA',id_ofs)

sort_ofs(ofs)

# for index in range(len(ofs_ret)):
#     print(ofs[ofs_ret[index]].descricao_material)
#     print(ofs[ofs_ret[index]].t_producao)

turno = 0

materiais=[]
dimensoes=[]
max_setups=50

for index in range(len(ofs_ret)):

    max_turno=len(maquinas[8].id_slot_inicio_turno)-1

    setup=10

    remanescente=ofs[ofs_ret[index]].t_producao+setup

    print('op' + str(ofs[ofs_ret[index]].cod_of) + ' of: ' + str(ofs[ofs_ret[index]].descricao_material) + ' turno: ' + str(turno))

    # print('tempo de produção: ' + str(remanescente))
    # print('material :' + str(ofs[ofs_ret[index]].material))
    # print('dimensao :' + str(ofs[ofs_ret[index]].dimensao))

    while remanescente>0 and turno<max_turno: #transformar em função

        # print((len(materiais)+len(dimensoes)))
        # print(materiais)
        # print(dimensoes)

        if ofs[ofs_ret[index]].material not in materiais and (len(materiais)+len(dimensoes)) < max_setups:

            materiais.append(ofs[ofs_ret[index]].material)
            materiais=list(set(materiais))
            # dimensoes.append(ofs[ofs_ret[index]].dimensao)
            # dimensoes = list(set(dimensoes))

        else:
            maquinas[8].vetor_materiais.append(materiais)
            turno+=1
            materiais=[]

        if maquinas[8].vetor_capacidade[turno]!=0:

            if ofs[ofs_ret[index]].id_alocada==0:
                ofs[ofs_ret[index]].id_alocada = 8
                ofs[ofs_ret[index]].id_slot_inicio_turno = maquinas[8].id_slot_inicio_turno[turno]

            remanescente = maquinas[8].diminuir_capacidade(turno, remanescente)

            if maquinas[8].vetor_capacidade[turno]==0:
                maquinas[8].vetor_materiais.append(materiais)
                turno+=1
                dimensoes=[]

        else:

            maquinas[8].vetor_materiais.append(materiais)
            turno += 1
            materiais = []
            dimensoes=[]



# for index in range(len(maquinas[8].id_slot_inicio_turno)):
#
#     print('materiais: ' + str(maquinas[8].vetor_materiais[index]))


for index in range(len(maquinas[8].id_slot_inicio_turno)):

    id_slot_inicio_turno = maquinas[8].id_slot_inicio_turno[index]
    lista_a_sortear=[]

    for id_of in range(len(ofs_ret)):

        if ofs[ofs_ret[id_of]].id_slot_inicio_turno==id_slot_inicio_turno:
            lista_a_sortear.append(ofs_ret[id_of])

    #print(lista_a_sortear)

for index in range(len(ofs_ret)):

    ofs[ofs_ret[index]].data_inicio = calcular_data_inicio(8, ofs_ret[index-1])
    print('of: ' + str(ofs[ofs_ret[index]].descricao_material) + 'data inicio: ' + str(ofs[ofs_ret[index]].data_inicio))
    ofs[ofs_ret[index]].data_fim = calcular_data_fim(ofs[ofs_ret[index]].data_inicio,ofs[ofs_ret[index]].t_producao + 10, 8)
    #print('data fim: ' + str(ofs[ofs_ret[index]].data_fim))

output = pd.DataFrame(columns=['Ordem de Produção', 'Tempo de Produção', 'Data Inicio', 'Data Fim' , 'Turno'])

for index in range(len(ofs_ret)):

    output = output.append({'Ordem de Produção': ofs[ofs_ret[index]].descricao_material, 'Tempo de Produção': ofs[ofs_ret[index]].t_producao,  'Data Inicio':ofs[ofs_ret[index]].data_inicio,'Data Fim':ofs[ofs_ret[index]].data_fim , 'Turno': slots[ofs[ofs_ret[index]].id_slot_inicio_turno].turno }, ignore_index=True)
    
output.to_csv('output.csv')














