import pandas as pd
from maquina import *
from of import *
from produto import *
from slot import *
from import_files import *


def definir_capacidade(id_maquina, id_turno): #define a capacidade da maquina no turno
    
    capacidade = 0

    for index in range(0, len(maquinas[id_maquina].vetor_slots)):
        if slots[maquinas[id_maquina].vetor_slots[index]].turno==id_turno:
            capacidade += slots[maquinas[id_maquina].vetor_slots[index]].fim - slots[maquinas[id_maquina].vetor_slots[index]].inicio

    maquinas[id_maquina].vetor_id_turno.appen(id_turno)
    maquinas[id_maquina].vetor_capacidade.appen(capacidade)

    return capacidade
