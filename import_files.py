import pandas as pd
from maquina import *
from of import *
from produto import *
from slot import *

produtos=[]
ofs=[]
maquinas=[]

def import_maquinas():

    df_maquinas = pd.read_csv('Maquinas.csv', sep=",")
    df_maquinas = df_maquinas.sort_values(by=['Máquina'])

    count_maquinas=0
    maquina_anterior=""
    grupo_maquinas=[]

    for index,row in df_maquinas.iterrows():

        if row['Máquina']==maquina_anterior:
            grupo_maquinas.append(row['Código'])

        else:
            new_maquina = maquina(count_maquinas, maquina_anterior,grupo_maquinas)
            maquinas.append(new_maquina)

            grupo_maquinas = []
            count_maquinas+=1
            grupo_maquinas.append(row['Código'])

        maquina_anterior=row['Máquina']

    return df_maquinas

import_maquinas()

def import_produtos():

    df_produtos=pd.read_csv('Controlo de Produção.csv',sep=",")
    df_produtos=df_produtos.sort_values(by=['BLOCO'])
    df_produtos['OBSERVAÇÕES'] = df_produtos['OBSERVAÇÕES'].astype(str)

    count_produtos=0
    count_ofs=0
    bloco_anterior=""

    # Cada produto corresponde a uma linha da df_produtos

    for index,row in df_produtos.iterrows():

        count_produtos+=1

        # Verificar se existe data de prioridade

        if 'PRIORIDADE' in row['OBSERVAÇÕES']:
            prioridade=row['OBSERVAÇÕES'].split("PRIORIDADE ", 1)[1]

        else:
            prioridade=""

        new_produto = produto(count_produtos-1, row['Descrição Material'], prioridade, row['Sem'], row['QTD'])
        produtos.append(new_produto)

        # Criar OF de serra ou laminadora

        if not pd.isnull(row['Serra/Lam']):
            count_ofs+=1
            new_of=of(count_ofs-1,row['Ordem Prod'],row[11])
            new_produto.adicionar_of(new_of)
            ofs.append(new_of)
            #ADICIONAR GET
            # lista=[x for x in maquinas if row['Serra/Lam'] in x.grupo]
            print(lista)

        # Criar OF da retificadora se não estiver vazia nem for igual à anterior

        if not pd.isnull(row['BLOCO']) and bloco_anterior!=row['Descrição Bloco']:

            count_ofs += 1
            new_of=of(count_ofs-1,row['Descrição Bloco'],row[18])
            new_produto.adicionar_of(new_of)
            ofs.append(new_of)
            bloco_anterior=row['Descrição Bloco']

        # Criar OF da lixadora

        if not pd.isnull(row['Lixadora']):

            count_ofs+=1
            new_of=of(count_ofs-1,row['Lixadora'],row[14])
            new_produto.adicionar_of(new_of)

    return df_produtos

import_produtos()
