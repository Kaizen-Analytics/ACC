import pandas as pd
from maquina import *
from of import *
from produto import *
from slot import *
from import_files import *
from functions import *

def sort_produtos():

    produtos.sort(key=lambda x: x.data_prioridade, reverse=False)


sort_produtos()

id_ofs_ret=[]
id_produtos_ret=[]

def get_min_slot(tempo,id_maquina):

    id_slot=-1

    for id_slot in maquinas[id_maquina].vetor_slots:
        if tempo>=slots[id_slot]:
            return id_slot

    return id_slot

for index in range(0,len(produtos)):

    for id_of in range(0,len(produtos[index].vetor_ofs)):
        if produtos[index].vetor_ofs[id_of].ct=='RETIFICADORA' and produtos[index].vetor_ofs[id_of] not in id_ofs_ret:
            id_ofs_ret.append(produtos[index].vetor_ofs[id_of])
            id_produtos_ret.append(produtos[index].id)

n_alocadas=0 #numero de ofs alocadas != do numero de produtos
n_ofs=len(id_ofs_ret)
distinct_refs=0

id_maquina=8

for index in range(0,len(maquinas[8].vetor_capacidade)):

    if maquinas[8].vetor_capacidade[index]>id_ofs_ret[n_alocadas].t_producao:








