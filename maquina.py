class maquina(object):

    def __init__(self,id,nome):
        self.nome=nome
        self.id = id
        self.vetor_slots=[]
        self.setups=[]
        self.vetor_capacidade=[]
        # setups diferentes turno. guardar dimensoes

    def __repr__(self):
        self.nome

    def adicionar_slots(self,slots):
        self.vetor_slots=slots

    def adicionar_setup(self,setup):
        self.setups.append(setup)

    def adicionar_inicio_turno(self):
        self.inicio_turno.append(0)





