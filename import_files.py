import pandas as pd
from maquina import *
from of import *
from produto import *
from slot import *

from datetime import datetime

produtos=[]
ofs=[]
maquinas=[]
slots=[]

format="%d/%m"
d1="09/02"
d1=datetime.strptime(d1, format)

#talvez faça mais sentido colocar um for em vez disto fora do import....
df_maquinas = pd.read_csv('Maquinas.csv', sep=",")
df_maquinas["index_maquina"] = ""
df_maquinas = df_maquinas.sort_values(by=['Máquina'])


def import_slots():

    df_slots = pd.read_csv('Slots.csv', sep=",")

    for index, row in df_slots.iterrows():
        new_slot = slot(row['index'], row['Inicio'], row['Fim'], row['Turno'])
        slots.append(new_slot)

    return df_slots

def import_maquinas():

    count_maquinas=0
    maquina_anterior=""

    for index,row in df_maquinas.iterrows():

        if row['Máquina'] != maquina_anterior:

            count_maquinas += 1
            new_maquina = maquina(count_maquinas-1, row['Máquina'])
            maquinas.append(new_maquina)
            lista_slots=import_slots()[import_slots()['Máquina']==row['Máquina']]['index'].tolist()
            new_maquina.adicionar_slots(lista_slots)

        df_maquinas.at[index, 'index_maquina'] = count_maquinas-1
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

        prioridade = 999999

        # Verificar se existe data de prioridade de inicio de produção

        if row['Sem']<6:
            prioridade = 0

        elif 'PRIORIDADE' in row['OBSERVAÇÕES']:
            prioridade=row['OBSERVAÇÕES'].split("PRIORIDADE ", 1)[1]
            prioridade = datetime.strptime(prioridade, format)
            prioridade=(prioridade-d1).total_seconds()/60

        new_produto = produto(count_produtos-1, row['Descrição Material'], prioridade, row['Sem'], row['QTD'])
        produtos.append(new_produto)

        # Criar OF de serra ou laminadora

        if not pd.isnull(row['Serra/Lam']):
            count_ofs+=1
            new_of=of(count_ofs-1,'Serra/Lam',row['Ordem Prod'],row[11])
            new_of.adicionar_maquinas(df_maquinas[df_maquinas['Código']==row['Serra/Lam']]['index_maquina'].tolist())
            new_produto.adicionar_of(new_of)
            ofs.append(new_of)

        # Criar OF da retificadora se não estiver vazia nem for igual à anterior

        if not pd.isnull(row['BLOCO']) and bloco_anterior!=row['Descrição Bloco']:

            count_ofs += 1
            new_of=of(count_ofs-1,'RETIFICADORA',row['Descrição Bloco'],row[18])
            new_of.adicionar_maquinas(df_maquinas[df_maquinas['Código'] == 'RETIFICADORA']['index_maquina'].tolist())
            new_produto.adicionar_of(new_of)
            ofs.append(new_of)
            bloco_anterior=row['Descrição Bloco']

        # Criar OF da lixadora

        if not pd.isnull(row['Lixadora']):

            count_ofs+=1
            new_of=of(count_ofs-1,'LIXADORA',row['Lixadora'],row[14])
            new_of.adicionar_maquinas(df_maquinas[df_maquinas['Código'] == 'LIXADORA']['index_maquina'].tolist())
            new_produto.adicionar_of(new_of)

    return df_produtos

import_produtos()


