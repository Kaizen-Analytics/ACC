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

def import_ofs():

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

        #new_produto = produto(count_produtos-1, row['Descrição Material'], prioridade, row['Sem'], row['QTD'])
        #produtos.append(new_produto)

        """Criar OF de serra ou laminadora"""

        if not pd.isnull(row['Serra/Lam']):

            of_serralam=of(count_ofs,'Serra/Lam',row['Ordem Prod'],row[11])
            of_serralam.adicionar_maquinas(df_maquinas[df_maquinas['Código']==row['Serra/Lam']]['index_maquina'].tolist())
            of_serralam.adicionar_produto(prioridade,row['Sem'])
            ofs.append(of_serralam)
            count_ofs += 1

        # Criar OF da retificadora se não estiver vazia nem for igual à anterior

        if not pd.isnull(row['BLOCO']) and bloco_anterior!=row['Descrição Bloco']:

            of_ret=of(count_ofs,'RETIFICADORA',row['Descrição Bloco'],800)
            of_ret.adicionar_maquinas(df_maquinas[df_maquinas['Código'] == 'RETIFICADORA']['index_maquina'].tolist())
            #new_produto.adicionar_of(new_of)
            ofs.append(of_ret)
            bloco_anterior=row['Descrição Bloco']
            count_ofs += 1

        if not pd.isnull(row['BLOCO']):

            of_ret.adicionar_produto(prioridade, row['Sem'])

        # Criar OF da lixadora

        if not pd.isnull(row['Lixadora']):

            of_lix=of(count_ofs,'LIXADORA',row['Lixadora'],row[14])
            of_lix.adicionar_maquinas(df_maquinas[df_maquinas['Código'] == 'LIXADORA']['index_maquina'].tolist())
            of_lix.adicionar_produto(prioridade, row['Sem'])
            ofs.append(of_lix)
            count_ofs += 1
            #new_produto.adicionar_of(new_of)

    return df_produtos



#of BL CC 8003/ORT 940X640X250 NE id=10
#retificadora id=10

# for index in range(len(ofs)):
#     print(ofs[index].id)
#     ofs[index].definir_data_min()
#     print(ofs[index].cod_of)
#     print(ofs[index].data_min)

# for index in range(len(maquinas)):
#     print(maquinas[index].nome)
#     for id_slot in range(len(maquinas[index].vetor_slots)):
#         print(str(slots[id_slot].inicio) + " " + str(slots[id_slot].fim))


