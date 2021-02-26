class maquina(object):

    def __init__(self,id,nome):
        self.nome=nome
        self.id = id
        self.vetor_slots=[]
        self.setups=[]
        self.vetor_capacidade=[]
        self.vetor_id_turno=[]
        # setups diferentes turno. guardar dimensoes

    def __repr__(self):
        self.nome

    def adicionar_slots(self,slots):
        self.vetor_slots=slots

    def adicionar_setup(self,setup):
        self.setups.append(setup)





