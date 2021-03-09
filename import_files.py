import pandas as pd
from maquina import *
from of import *
from produto import *
from slot import *
from datetime import datetime
import math

produtos=[]
ofs=[]
maquinas=[]
slots=[]

format="%d/%m"
d1="01/03"
d1=datetime.strptime(d1, format)

def import_slots():

    df_slots = pd.read_csv('Slots.csv', sep=",")
    df_slots["index"] = ""
    count_slots=0

    for index, row in df_slots.iterrows():
        new_slot = slot(count_slots, row['Máquina'], row['Inicio'], row['Fim'], row['Turno'])
        slots.append(new_slot)
        df_slots.at[index,'index']=count_slots
        count_slots+=1

    return df_slots

def import_maquinas():

    df_maquinas = pd.read_csv('Maquinas.csv', sep=",")
    df_maquinas["index_maquina"] = ""
    df_maquinas = df_maquinas.sort_values(by=['Máquina'])

    count_maquinas=0

    for index,row in df_maquinas.iterrows():

        new_maquina = maquina(count_maquinas,row['Código'], row['Máquina'],0.9)
        maquinas.append(new_maquina)
        lista_slots=import_slots()[import_slots()['Máquina']==row['Máquina']]['index'].tolist()
        new_maquina.adicionar_slots(lista_slots)
        df_maquinas.at[index, 'index_maquina'] = count_maquinas
        count_maquinas += 1

    return df_maquinas

import_slots()
df_maquinas=import_maquinas()

def import_ofs():

    count_ofs = 0
    id_precedencia=[]

    #LER NECESSIDADES PLACAS

    df_placas=pd.read_csv('Placas_CNM_W0921.csv',sep=",")
    df_placas['OBSERVAÇÕES'] = df_placas['OBSERVAÇÕES'].astype(str)

    for index, row in df_placas.iterrows():

        #verificar a prioridade do produto final

        prioridade = 999999

        if row['SEM'] < 9:
            prioridade = (0-d1).total_seconds()/60

        elif 'PRIORIDADE' in row['OBSERVAÇÕES']:
            prioridade=row['OBSERVAÇÕES'].split("PRIORIDADE ", 1)[1]
            prioridade = datetime.strptime(prioridade, format)
            prioridade=(prioridade-d1).total_seconds()/60

        #adicionar ofs por precedências

        #1. retificadora
        #self,id, ct,cod_of,descricao_material,t_producao

        if not pd.isnull(row['BLOCO']):
            of_ret = of(count_ofs, 'RETIFICADORA', row['BLOCO'], row[17],math.ceil(row['QTD BL.'])*0.22*60,[],prioridade)
            of_ret.adicionar_maquinas(df_maquinas[df_maquinas['Código'] == 'RETIFICADORA']['index_maquina'].tolist())
            ofs.append(of_ret)
            id_precedencia.append(count_ofs)
            count_ofs += 1

        # 2.Serra
        # self,id, ct,cod_of,descricao_material,t_producao

        if not pd.isnull(row['SERRA/LAM']):
            of_serra_lam = of(count_ofs, row['CT'], row['SERRA/LAM'], row['Descrição Material'], row[14]*60, id_precedencia,prioridade)
            of_serra_lam.adicionar_maquinas(df_maquinas[df_maquinas['Código'] == row['CT']]['index_maquina'].tolist())
            ofs.append(of_serra_lam)
            id_precedencia.append(count_ofs)
            count_ofs += 1

        # 3.Lixadora
        if not pd.isnull(row['OF Lixadora']):
            of_lixadora = of(count_ofs, 'LIXADORA', row['OF Lixadora'], row['Descrição Material'], row[17]*60, id_precedencia,prioridade)
            of_lixadora.adicionar_maquinas(df_maquinas[df_maquinas['Código'] == 'LIXADORA']['index_maquina'].tolist())
            ofs.append(of_lixadora)
            count_ofs += 1

        id_precedencia=[]

    # LER NECESSIDADES CSS

    df_css = pd.read_csv('CCS_CNM_W0921.csv', sep=",")

    for index, row in df_css.iterrows():

        #verificar a prioridade do produto final

        prioridade = 999999

        if 'Até' in row['Data solicitada']:
            prioridade=row['Data solicitada'].split("Até ", 1)[1]
            d = "01/03/2021"
            d = datetime.strptime(d, '%d/%m/%Y')
            prioridade = datetime.strptime(prioridade, '%d/%m/%Y')
            prioridade=(prioridade-d).total_seconds()/60


        elif pd.isnull(row['Data solicitada'])==False:
            d = "01/03/2021"
            d = datetime.strptime(d, '%d/%m/%Y')
            prioridade = datetime.strptime(row['Data solicitada'], '%d/%m/%Y')
            prioridade = (prioridade-d).total_seconds()/60


        #adicionar ofs por precedências

        #1. retificadora
        #self,id, ct,cod_of,descricao_material,t_producao

        if not pd.isnull(row['Bloco']):
            of_ret = of(count_ofs, 'RETIFICADORA', row['Bloco'], row[12],math.ceil(row['QTD BL.'])*0.22*60,[],prioridade)
            of_ret.adicionar_maquinas(df_maquinas[df_maquinas['Código'] == 'RETIFICADORA']['index_maquina'].tolist())
            ofs.append(of_ret)
            id_precedencia.append(count_ofs)
            count_ofs += 1

        # 2.Serra e Lixadora
        # self,id, ct,cod_of,descricao_material,t_producao

        if not pd.isnull(row['Centro trabalho']):
            of_serra_lam = of(count_ofs, row['Centro trabalho'], row['Ordem Produção'], row['Descrição Material'], row['Hrs']*60, id_precedencia,prioridade)
            of_serra_lam.adicionar_maquinas(df_maquinas[df_maquinas['Código'] == row['Centro trabalho']]['index_maquina'].tolist())
            ofs.append(of_serra_lam)
            id_precedencia.append(count_ofs)
            count_ofs += 1

        id_precedencia=[]

        # LER NECESSIDADES BLOCOS INTEIROS

        df_blocos = pd.read_csv('BL INTEIROS_CNM_W0921.csv', sep=",")

        for index, row in df_blocos.iterrows():

            # verificar a prioridade do produto final

            prioridade = 999999

            if row['SEM'] < 9:
                prioridade = (0 - d1).total_seconds() / 60

            # adicionar ofs por precedências

            # 1. retificadora
            # self,id, ct,cod_of,descricao_material,t_producao

            if not pd.isnull(row['Item']):
                of_ret = of(count_ofs, 'RETIFICADORA', row['Material'], row['Desc. Material'], math.ceil(row['QTD']) * 0.22 * 60, [],prioridade)
                of_ret.adicionar_maquinas(df_maquinas[df_maquinas['Código'] == 'RETIFICADORA']['index_maquina'].tolist())
                ofs.append(of_ret)
                count_ofs += 1

    return df_placas

import_ofs()

