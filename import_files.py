import pandas as pd
from maquina import *
from of import *
from produto import *
from slot import *

def import_produtos():

    df_produtos=pd.read_csv('Controlo de Produção.csv',sep=",")
    df_produtos['OBSERVAÇÕES'] = df_produtos['OBSERVAÇÕES'].astype(str)

    count_produtos=0
    count_ofs=0

    # Cada produto corresponde a uma linha da df_produtos

    for index,row in df_produtos.iterrows():

        count_produtos+=1

        # Verificar se existe data de prioridade

        if 'PRIORIDADE' in row['OBSERVAÇÕES']:
            prioridade=row['OBSERVAÇÕES'].split("PRIORIDADE ", 1)[1]

        else:
            prioridade=""

        new_produto = produto(count_produtos, row['Descrição Material'], prioridade, row['Sem'], row['QTD'])

        # Criar OF de serra ou laminadora

        if not pd.isnull(row['Serra/Lam']):
            count_ofs+=1
            new_of=of(count_ofs, row['Serra/Lam'],row['Ordem Prod'],row[11])
            new_produto.adicionar_of(new_of)

        # Criar OF da retificadora

        if not pd.isnull(row['BLOCO']):
            count_ofs+=1
            new_of=of(count_ofs, 'Retificadora',row['Descrição Bloco'],row[18])
            new_produto.adicionar_of(new_of)

        # Criar OF da lixadora

        if not pd.isnull(row['Lixadora']):
            count_ofs+=1
            new_of=of(count_ofs,'Lixadora',row['Lixadora'],row[14])
            new_produto.adicionar_of(new_of)

    return df_produtos

import_produtos()

