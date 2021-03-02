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

sort_ofs(ofs)

id_ofs=get_ids(ofs)

ofs_ret=filter_ofs('RETIFICADORA',id_ofs)

turno = 0

for index in range(len(ofs_ret)):

    max_turno=len(maquinas[8].id_slot_inicio_turno)-1
    setup=10
    remanescente=ofs[ofs_ret[index]].t_producao+setup

    while remanescente>0 and turno<max_turno: #transformar em função

        if maquinas[8].vetor_capacidade[turno]!=0:

            if ofs[ofs_ret[index]].id_alocada==0:
                ofs[ofs_ret[index]].id_alocada = 1
                ofs[ofs_ret[index]].id_slot_inicio_turno = maquinas[8].id_slot_inicio_turno[turno]

                #alterar index-1 - pode nao ser feasible
                ofs[ofs_ret[index]].data_inicio = calcular_data_inicio(8,index-1,index)

                print('id slot inicial:' + str(ofs[ofs_ret[index]].id_slot_inicio_turno))
                print('data inicio: ' + str(ofs[ofs_ret[index]].data_inicio))

            remanescente = maquinas[8].diminuir_capacidade(turno, remanescente)

            if maquinas[8].vetor_capacidade[turno]==0:

                turno+=1

        else:

            turno += 1

    ofs[ofs_ret[index]].data_fim = calcular_data_fim(ofs[ofs_ret[index]].data_inicio,ofs[ofs_ret[index]].t_producao+setup, 8)

# def get_of_min(vetor_id):
#
#     n_ofs=len(vetor_id)
#     id_next_of=0
#     data_min=99999
#
#     for index in range(n_produtos):
#         if vetor_id[index].data_prioridade<data_min and vetor_id[]
#
#     produtos.sort(key=lambda x: x.data_prioridade, reverse=False)
#     #ordenar ids, nao vetor
#
# def get_of_data_min():
#
#     #Vai buscar o delta mais curto da lista de produtos da OF
#
#
#
# id_ofs_ret=[]
# id_produtos_ret=[]
#
# def get_min_slot(tempo,id_maquina):
#
#     id_slot=-1
#
#     for id_slot in maquinas[id_maquina].vetor_slots:
#         if tempo>=slots[id_slot]:
#             return id_slot
#
#     return id_slot
#
# for index in range(0,len(produtos)): #função verificar ofs retificadora
#
#     for id_of in range(0,len(produtos[index].vetor_ofs)):
#         if produtos[index].vetor_ofs[id_of].ct=='RETIFICADORA' and produtos[index].vetor_ofs[id_of] not in id_ofs_ret:
#             id_ofs_ret.append(produtos[index].vetor_ofs[id_of])
#             id_produtos_ret.append(produtos[index].id)
#
# n=0 #numero de ofs alocadas != do numero de produtos
# n_ofs=len(id_ofs_ret)
#
# distinct_refs=[]
# refs_turno=[]
# lim_refs=2
#
#
# id_maquina=8 #Criar função para guardar id retificadora
#
# for index in range(0,len(maquinas[8].vetor_id_turno)):
#
#     #o index é partilhado pelo turno e pela capacidade
#
#     setup=10
#
#     while maquinas[8].vetor_capacidade[index]!=0:
#
#         if id_ofs_ret[n].cod_of not in distinct_refs[maquinas[8].vetor_id_turno[index]]:
#
#             distinct_refs[maquinas[8].vetor_id_turno[index]]+=1
#
#             #setup=get_setup(dim1,dim2)
#
#             setup=90
#
#         if maquinas[8].vetor_capacidade[index]>id_ofs_ret[n].t_producao+setup and len(distinct_refs)<3:
#
#         n += 1












