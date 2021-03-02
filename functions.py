import pandas as pd
from maquina import *
from of import *
from produto import *
from slot import *
from import_files import *

def get_ids(vetor):

    ids=[]

    for index in range(len(vetor)):
        ids.append(vetor[index].id)

    return ids

def filter_ofs(ct,ids):

    ids=[]

    for index in range(len(ofs)):

        if ofs[index].ct==ct:
            ids.append(ofs[index].id)


    return ids

def sort_ofs(vetor_ofs):

    vetor_ofs.sort(key=lambda x: x.data_min, reverse=True)

def definir_data_of(id_of):

    n_produtos=len(produtos)
    for index in range(n_produtos):
        o=0

def definir_capacidade(id_maquina, id_turno): #define a capacidade da maquina no turno
    
    capacidade = 0

    for index in range(0, len(maquinas[id_maquina].vetor_slots)):
        if slots[maquinas[id_maquina].vetor_slots[index]].turno==id_turno:
            capacidade += slots[maquinas[id_maquina].vetor_slots[index]].fim - slots[maquinas[id_maquina].vetor_slots[index]].inicio

    maquinas[id_maquina].vetor_id_turno.appen(id_turno)
    maquinas[id_maquina].vetor_capacidade.appen(capacidade)

    return capacidade

def tomins(data):

    if isinstance(data,int):

        #Se a data for semana, tem de ser convertida em mins para sexta
        return 0

    else:

        #se a data for uma prioridade (data) tem ser convertida em mins para esse dia
        return 0

def definir_capacidades():

    for index in range(len(maquinas)):

        turnos = []

        for i in range(len(maquinas[index].vetor_slots)):

            capacidade = slots[maquinas[index].vetor_slots[i]].fim - slots[maquinas[index].vetor_slots[i]].inicio

            if slots[maquinas[index].vetor_slots[i]].turno in turnos:

                id_turno = turnos.index(slots[maquinas[index].vetor_slots[i]].turno)

                maquinas[index].update_turno(id_turno, capacidade)

            else:

                turnos.append(slots[maquinas[index].vetor_slots[i]].turno)

                maquinas[index].adicionar_turno(slots[maquinas[index].vetor_slots[i]].id, capacidade)

def calcular_data_inicio(id_maquina,id_ultimo_alocado,id_alocar):

    #fornece id anterior e id a alocar porque pode o index-1 ser impossível

    if id_ultimo_alocado<0:
        #primeiro alocado
        ofs[id_alocar].data_inicio=slots[maquinas[id_maquina].vetor_slots[0]].inicio
    else:
        id_slot=ofs[id_ultimo_alocado].id_slot_inicio_turno
        #a of pode começar no ultimo minuto da slot? se sim colocar if !!!!!
        ofs[id_alocar].data_inicio = ofs[id_ultimo_alocado].data_fim+1


def calcular_data_fim(t_start,tempo_teorico, id_maquina):
    # Percorrer as slots e determinar o momento final (não considerar ocupação)
    maq = maquinas[id_maquina]

    # Calculo tempo a alocar= setup da máquina + tempo produtivo
    tempo_alocar = tempo_teorico

    n_slots = len(maq.vetor_slots)
    t_finish = t_start
    tempo_em_falta = tempo_alocar
    index = 0

    # Percorrer as várias slots at++e determinar o momento final
    while index <= n_slots and tempo_em_falta > 0:
        slot = slots[maquinas[id_maquina].vetor_slots[index]]
        s_slot = slot.inicio
        f_slot = slot.fim

        # Se for Slot Inicial
        if t_start >= s_slot and t_start <= f_slot:

            if f_slot - t_start <= tempo_em_falta:  # Se couber na primeira slot
                t_finish = t_start + tempo_em_falta
                tempo_em_falta = 0
            else:
                tempo_em_falta = tempo_em_falta - (f_slot - t_start)

        elif t_start <= s_slot:

            if f_slot - s_slot <= tempo_em_falta:  # Se o restante couber na slot
                t_finish = s_slot + tempo_em_falta
                tempo_em_falta = 0
            else:
                tempo_em_falta = tempo_em_falta - (f_slot - s_slot)
        # Incremento
        index += 1

    if t_finish > 0:
        return t_finish
    else:
        print("Erro ao calcular calculo_finish_from_start")
        return -1

