class maquina(object):

    def __init__(self,id,nome):
        self.nome=nome
        self.id = id
        self.vetor_slots=[]
        self.setups=[]
        self.vetor_capacidade=[]
        self.id_slot_inicio_turno=[]
        # setups diferentes turno. guardar dimensoes

    def __repr__(self):
        self.nome

    def adicionar_slots(self,slots):
        self.vetor_slots=slots

    def adicionar_setup(self,setup):
        self.setups.append(setup)

    def adicionar_turno(self,id_slot,capacidade):
        self.vetor_capacidade.append(capacidade)
        self.id_slot_inicio_turno.append(id_slot)

    def update_turno(self,index,capacidade):
        self.vetor_capacidade[index]+=capacidade

    def diminuir_capacidade(self,index,capacidade):

        #print('capacidade in: ' +str(self.vetor_capacidade[index]) + 'turno' + str(index) )

        if capacidade>self.vetor_capacidade[index]:

            remanescente=capacidade - self.vetor_capacidade[index]
            self.vetor_capacidade[index] = 0
            #retorna remanescente
            #print('capacidade out: ' + str(self.vetor_capacidade[index])+ 'turno' + str(index))
            #print('remanescente: ' + str(remanescente))
            return remanescente

        else:
            self.vetor_capacidade[index] = self.vetor_capacidade[index] - capacidade
            #print('capacidade out: ' + str(self.vetor_capacidade[index])+ 'turno' + str(index))
            #print('remanescente: ' + str(0))
            return 0











